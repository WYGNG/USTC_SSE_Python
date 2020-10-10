import tensorflow as tf
import numpy as np

'''
函数，同AlexNet
'''
def conv(x,filter_height,filter_width,num_filters,stride_y,stride_x,name,padding="SAME",groups=1):
    #获取输入tensor的channel
    input_channels = int(x.get_shape()[-1])

    #创建一个lambda函数
    convolve = lambda i,k:tf.nn.conv2d(i,k,strides=[1,stride_y,stride_x,1],padding=padding)
    with tf.variable_scope(name) as scope:
        #定义权重
        weights = tf.get_variable("weights",shape=[filter_height,filter_width,
                                                   input_channels/groups,num_filters])
        #定义偏置
        biases = tf.get_variable("biases",shape=[num_filters])

    if groups == 1:
        conv = convolve(x,weights)
    else:
        input_groups = tf.split(axis=3,num_or_size_splits=groups,value=x)
        weight_groups = tf.split(axis=3,num_or_size_splits=groups,value=weights)
        output_groups = [convolve(i,k) for i,k in zip(input_groups,weight_groups)]
        #连接卷积层
        conv = tf.concat(axis=3,values=output_groups)
    bias = tf.reshape(tf.nn.bias_add(conv,biases),tf.shape(conv))
    #relu激活函数
    relu = tf.nn.relu(bias,name=scope.name)

    return relu

'''
全连接层函数
'''
def fc(x,num_in,num_out,name,relu=True):
    with tf.variable_scope(name) as scope:
        #定义权重和偏置
        weights = tf.get_variable("weights",shape=[num_in,num_out],trainable=True)
        biases = tf.get_variable("biases",[num_out],trainable=True)
        fc_out = tf.nn.xw_plus_b(x,weights,biases,name=scope.name)
    if relu:
        fc_out = tf.nn.relu(fc_out)
    return fc_out


'''
最大池化层函数
'''
def max_pool(x,filter_height,filter_width,stride_y,stride_x,name,padding="SAME"):
    return tf.nn.max_pool(x,ksize=[1,filter_height,filter_width,1],strides=[1,stride_y,stride_x,1],
                          padding=padding,name=name)

'''
lrn层
'''
def lrn(x,radius,alpha,beta,name,bias=1.0):
    return tf.nn.local_response_normalization(x,depth_radius=radius,alpha=alpha,beta=beta,bias=bias,name=name)

'''
dropout层
'''
def dropout(x,keep_prob):
    return tf.nn.dropout(x,keep_prob)


'''
定义VggNet类
'''
class VggNet(object):
    '''

    参数：
    x:输入的tensor
    keep_prob:dropout节点保留概率
    num_classes:需要分类的数量
    skip_layer:需要重新训练的层
    weights_path:预训练参数文件的路径
    '''
    def __init__(self,x,keep_prob,num_classes,skip_layer,weights_path="default"):
        self.X = x
        self.KEEP_PROB = keep_prob
        self.NUM_CLASSES = num_classes
        self.SKIP_LAYER = skip_layer

        if weights_path == "default":
            self.WEIGHTS_PATH = "model/VGG16.npy"
        else:
            self.WEIGHTS_PATH = weights_path
        self.create()

    '''
    
    '''
    def create(self):
        #第一层
        conv1_1 = conv(self.X,3,3,64,1,1,padding="VALID",name="conv1")
        conv1_2 = conv(conv1_1, 3, 3, 64, 1, 1, padding="VALID", name="conv1")
        pool1 = max_pool(conv1_2,2,2,2,2,padding="VALID",name="pool1")

        #第二层
        conv2_1 = conv(pool1,3,3,128,1,1,groups=2,name="conv2")
        conv2_2 = conv(conv2_1, 3, 3, 128, 1, 1, groups=2, name="conv2")
        pool2 = max_pool(conv2_2,2,2,2,2,padding="VALID",name="pool2")

        #第三层
        conv3_1 = conv(pool2,3,3,256,1,1,name="conv3")
        conv3_2 = conv(conv3_1, 3, 3, 256, 1, 1, name="conv3")
        conv3_3 = conv(conv3_2, 3, 3, 256, 1, 1, name="conv3")
        pool3 = max_pool(conv3_3, 2, 2, 2, 2, padding="VALID", name="pool2")

        #第四层

        conv4_1 = conv(pool3,3,3,512,1,1,name="conv3")
        conv4_2 = conv(conv4_1, 3, 3, 512, 1, 1, name="conv3")
        conv4_3 = conv(conv4_2, 3, 3, 512, 1, 1, name="conv3")
        pool4 = max_pool(conv4_3, 2, 2, 2, 2, padding="VALID", name="pool2")

        #第五层
        conv5_1 = conv(pool4,3,3,512,1,1,name="conv3")
        conv5_2 = conv(conv5_1, 3, 3, 512, 1, 1, name="conv3")
        conv5_3 = conv(conv5_2, 3, 3, 512, 1, 1, name="conv3")
        pool5 = max_pool(conv5_3, 2, 2, 2, 2, padding="VALID", name="pool2")

        #第六层,全连接层
        flattened = tf.reshape(pool5,[-1,7*7*512])
        fc6 = fc(flattened,7*7*512,4096,name="fc6")
        dropout6 = dropout(fc6,self.KEEP_PROB)

        #第七层，全连接层
        fc7 = fc(dropout6,4096,4096,name="fc7")
        dropout7 = dropout(fc7,self.KEEP_PROB)

        #第八层,全连接层
        self.fc8 = fc(dropout7,4096,self.NUM_CLASSES,relu=False,name="fc8")

    '''
    加载预训练权重文件初始化权重
    '''
    def load_initial_weights(self,session):
        #加载预训练权重文件
        weights_dict = np.load(self.WEIGHTS_PATH,encoding="bytes").item()
        #遍历所有的层,看是否需要重新训练
        for op_name in weights_dict:
            if op_name not in self.SKIP_LAYER:
                with tf.variable_scope(op_name,reuse=True):
                    for data in weights_dict[op_name]:
                        if len(data.shape) == 1:
                            var = tf.get_variable("biases",trainable=False)
                            session.run(var.assign(data))
                        else:
                            var = tf.get_variable("weights",trainable=False)
                            session.run(var.assign(data))
