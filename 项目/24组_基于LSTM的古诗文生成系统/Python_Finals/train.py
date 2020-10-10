# -*- coding: utf-8 -*-
import os
import tensorflow as tf
from dispose_data import process_poetry, get_batch

batch_size = 64
epochs = 40
model_path = os.path.abspath('./model/seven_jue')
file_path = os.path.abspath('./data/qijue_all.txt')
learning_rate = 1e-4


def model(input_data, words_len, rnn_size, num_layers, batch):
    # 定義模型
    cell = tf.contrib.rnn.LSTMCell(rnn_size, state_is_tuple=True)
    cell = tf.contrib.rnn.MultiRNNCell([cell] * num_layers, state_is_tuple=True)
    initial_state = cell.zero_state(batch, tf.float32)           # 输出大小为batch_size的零state tensor
    embedding = tf.get_variable(
        'embedding',
        initializer=tf.random_uniform([words_len, rnn_size],
                                      -1.0, 1.0))                # 返回一个[words_len, 128]的二维张量，值在-1，1之间均匀分布
    inputs = tf.nn.embedding_lookup(embedding, input_data)       # [all_words_len, 128], [64, 行长] input:(64, ?, 128)

    outputs, last_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=initial_state,)  # [64, ?, 128]  ?为行长
    output = tf.reshape(outputs, [-1, rnn_size])                                         # [?, 128]      ?为行长×64
    weights = tf.Variable(tf.truncated_normal([rnn_size, words_len]))                    # [128, words_len]，正态分布
    bias = tf.Variable(tf.zeros(shape=[words_len]))
    losses = tf.nn.bias_add(tf.matmul(output, weights), bias=bias)                       # [?, words_len], 此为模型输出值
    return losses, initial_state, last_state


def training():
    # 訓練
    vector, word_dic, words = process_poetry(file_path, '7jue')                  # 调用数据預处理函数，需附加詩文種類
    batches_inputs, batches_outputs = get_batch(batch_size, vector, word_dic)    # 获得训练数据和标签
    input_data = tf.placeholder(tf.int32, [batch_size, None])                    # 输入数据占位符 (64,行长）
    output_targets = tf.placeholder(tf.int32, [batch_size, None])                # 标签占位符     (64,行长）
    loss, _, last_state = model(input_data=input_data, words_len=len(words), rnn_size=128, num_layers=2, batch=64)
    labels = tf.one_hot(tf.reshape(output_targets, [-1]), depth=len(words))      # 標簽需要独热处理

    loss = tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=loss)   # 交叉熵損失函數
    loss_ = tf.reduce_mean(loss)                                                 # [?, words_len]，损失函数
    train_op = tf.train.AdamOptimizer(learning_rate).minimize(loss_)             # 優化

    saver = tf.train.Saver(tf.global_variables())
    init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    with tf.Session() as sess:
        sess.run(init_op)                                                        # 开启会话
        n = len(vector) // batch_size                                            # 每轮训练的次数
        for epoch in range(1, epochs+1):
            m = 0
            for batch in range(n):
                losses, _, _ = sess.run([loss_, last_state, train_op],
                                        feed_dict={input_data: batches_inputs[m],
                                        output_targets: batches_outputs[m]})
                m += 1
                print('Epoch: %d, batch: %d, training loss: %.5f' % (epoch, batch, losses))
            if epoch % 5 == 0:
                saver.save(sess, os.path.join(model_path, 'poems'), global_step=epoch)


if __name__ == '__main__':
    training()

