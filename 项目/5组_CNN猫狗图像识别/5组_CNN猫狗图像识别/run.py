import os
import numpy as np
import tensorflow as tf
from AlexNet import AlexNet
from vgg import VggNet
from DataGenerator import ImageDataGenerator
from util_data import get_img_infos,split_dataset
from datetime import datetime
import pandas as pd
from Exploration import show_part_image,classifiction_report_info,val_pred_and_real_distribution

import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"]=["SimHei"]

# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

#设置训练文件的路径
train_txt = "txt/train.txt"
test_txt = "txt/test.txt"

learning_rate = 0.0001
num_epochs = 40
batch_size = 20

dropout_rate = 0.5
num_classes = 2
train_layers = ["fc6","fc7","fc8"]

#设置训练多少次保存tensor board
display_step = 20

filewrite_path = "tensorboard"
checkpoint_path = "checkpoints"

#判断目录是否存在
if not os.path.isdir(filewrite_path):
    os.mkdir(filewrite_path)
if not os.path.isdir(checkpoint_path):
    os.mkdir(checkpoint_path)


x = tf.placeholder(tf.float32,[None,227,227,3])
y = tf.placeholder(tf.float32,[None,num_classes])
keep_prob = tf.placeholder(tf.float32)
model = AlexNet(x,keep_prob,num_classes,train_layers)
# model = VggNet(x,keep_prob,num_classes,train_layers)
#获取最后一层全连接层的输出结果
output_y = model.fc8
#计算输出的标签
output_label = tf.argmax(output_y,1)

#训练模型
def train():
    label_name_to_num = {"dog":1,"cat":0}
    #获取所有的训练数据
    img_ids,img_labels,img_paths = get_img_infos("train",train_txt,label_name_to_num)
    train_dataset,val_dataset = split_dataset(img_ids,img_paths,img_labels)
    print(train_dataset)
    with tf.device("/cpu:0"):
        train_data = ImageDataGenerator(train_dataset,mode="train",batch_size=batch_size,num_classes=num_classes,
                                        shuffle=True)
        val_data = ImageDataGenerator(val_dataset,mode="val",batch_size=batch_size,num_classes=num_classes)
        #创建一个获取下一个batch的迭代器
        iterator = tf.data.Iterator.from_structure(train_data.data.output_types,train_data.data.output_shapes)
        next_batch = iterator.get_next()

    #初始化训练集数据
    training_init_op = iterator.make_initializer(train_data.data)
    #初始化测试集数据
    val_init_op = iterator.make_initializer(val_data.data)
    #获取需要重新训练的变量
    var_list = [v for v in tf.trainable_variables() if v.name.split("/")[0] in train_layers]
    #定义交叉熵损失值
    with tf.name_scope("cross_entropy_loss"):
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=output_y,labels=y))
    #更新变量
    with tf.name_scope("train"):
        #计算需要更新变量的梯度
        gradients = tf.gradients(loss,var_list)
        gradients = list(zip(gradients,var_list))
        #更新权重
        # optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        # train_op = optimizer.apply_gradients(grads_and_vars=gradients)

        train_op = tf.train.AdamOptimizer(learning_rate).minimize(loss)

    for gradient,var in gradients:
        tf.summary.histogram(var.name+"/gradient",gradient)

    for var in var_list:
        tf.summary.histogram(var.name,var)

    tf.summary.scalar("cross_entropy",loss)

    #计算准确率
    with tf.name_scope("accuracy"):
        correct_pred = tf.equal(tf.argmax(output_y,1),tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct_pred,tf.float32))

    tf.summary.scalar("accuracy",accuracy)

    merged_summary = tf.summary.merge_all()

    writer = tf.summary.FileWriter(filewrite_path)

    saver = tf.train.Saver()
    #计算每轮的迭代次数
    train_batches_per_epoch = int(np.floor(train_data.data_size/batch_size))
    val_batches_per_epoch = int(np.floor(val_data.data_size/batch_size))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer.add_graph(sess.graph)
        model.load_initial_weights(sess)

        #记录最好的验证准确率
        best_val_acc = 0.9
        print('开始训练')
        #迭代训练
        for epoch in range(num_epochs):
            sess.run(training_init_op)
            for step in range(train_batches_per_epoch):
                # print('0batch')
                img_batch,label_batch = sess.run(next_batch)
                sess.run(train_op,feed_dict={x:img_batch,y:label_batch,keep_prob:dropout_rate})
                if step % display_step == 0:
                    s,train_acc,train_loss = sess.run([merged_summary,accuracy,loss],
                                                feed_dict={x:img_batch,y:label_batch,keep_prob:1.0})
                    writer.add_summary(s,epoch*train_batches_per_epoch+step)
            sess.run(val_init_op)
            #统计验证集的准确率
            val_acc = 0
            #统计验证集的损失值
            val_loss = 0
            test_count = 0
            for _ in range(val_batches_per_epoch):
                img_batch,label_batch = sess.run(next_batch)
                acc,val_batch_loss = sess.run([accuracy,loss],feed_dict={x:img_batch,y:label_batch,keep_prob:1.0})
                val_acc += acc
                val_loss += val_batch_loss
                test_count += 1
            val_acc /= test_count
            val_loss /= test_count
            print("%s epoch:%d,train acc:%.4f,train loss:%.4f,val acc:%.4f,val loss:%.4f"
                  %(datetime.now(),epoch+1,train_acc,train_loss,val_acc,val_loss))

            if val_acc > best_val_acc:
                checkpoint_name = os.path.join(checkpoint_path,"model_epoch%s_%.4f.ckpt"%(str(epoch+1),val_acc))
                saver.save(sess,checkpoint_name)
                best_val_acc = val_acc

#预测测试集生成结果
def genrate_pre_result():
    #获取需要预测结果的所有数据
    img_ids,_,img_paths = get_img_infos("test",test_txt)
    test_dataset = pd.DataFrame({"img_id":img_ids,"img_path":img_paths})
    with tf.device("/cpu:0"):
        test_data = ImageDataGenerator(test_dataset,mode="test",batch_size=batch_size,num_classes=num_classes)
        iterator = tf.data.Iterator.from_structure(test_data.data.output_types,test_data.data.output_shapes)
        next_batch = iterator.get_next()
    #初始化测试集中的图片数据
    test_init_op = iterator.make_initializer(test_data.data)
    #创建一个加载模型文件的对象
    saver = tf.train.Saver()
    #用来保存图片的id
    test_img_ids = []
    #用来保存图片的预测结果
    test_pred_labels = []
    #计算需要迭代的次数
    steps = (test_data.data_size-1) // batch_size + 1
    #设置模型文件的路径
    model_path = "checkpoints/model_epoch37_0.9275.ckpt"
    print('加载完成')
    with tf.Session() as sess:
        sess.run(test_init_op)
        #加载模型文件
        saver.restore(sess,model_path)
        for step in range(steps):
            #获取数据
            image_data,image_id = sess.run(next_batch)
            #预测图片的标签
            pred_label = sess.run(output_y,feed_dict={x:image_data,keep_prob:1.0})
            pred_prob = tf.nn.softmax(pred_label)
            #保存预测的结果
            test_img_ids.extend(image_id)
            test_pred_labels.extend(np.round(sess.run(pred_prob)[:,1],decimals=2))
        data = pd.DataFrame({"id":test_img_ids,"label":test_pred_labels})
        data.sort_values(by="id",ascending=True,inplace=True)
        #保存结果
        data.to_csv("AlexNet_transfer2.csv",index=False)

#评估验证集的预测结果
def evaluation_eval_dataset():
    #读取验证集的csv文件
    data = pd.read_csv("txt/val.csv",index_col=False)
    with tf.device("/cpu:0"):
        val_data = ImageDataGenerator(data,mode="val",batch_size=batch_size,num_classes=num_classes)
        iterator = tf.data.Iterator.from_structure(val_data.data.output_types,val_data.data.output_shapes)
        next_batch = iterator.get_next()
    val_init_op = iterator.make_initializer(val_data.data)
    saver = tf.train.Saver()
    steps = (val_data.data_size-1) // batch_size + 1
    #用来保存预测的类标结果
    val_pred_label = []
    #用来保存真实的结果
    val_real_label = []
    #用来保存图片的路径

    #设置模型文件的路径
    model_path = "checkpoints/model_epoch1_0.9187.ckpt"
    with tf.Session() as sess:
        sess.run(val_init_op)
        saver.restore(sess,model_path)
        for step in range(steps):
            #获取数据
            img_data,img_label = sess.run(next_batch)
            #预测类标
            pred_label = sess.run(output_label,feed_dict={x:img_data,keep_prob:1.0})
            val_real_label.extend(np.argmax(img_label,axis=1))
            val_pred_label.extend(pred_label)
    #展示部分图片的预测结果
    show_part_image(val_pred_label,val_real_label,data.img_path.tolist())
    #展示预测结果的分布情况
    val_pred_and_real_distribution(val_pred_label,val_real_label)
    #展示分类结果报告
    classifiction_report_info(val_pred_label,val_real_label)



if __name__ == "__main__":
    # train()
    genrate_pre_result()
    #evaluation_eval_dataset()
