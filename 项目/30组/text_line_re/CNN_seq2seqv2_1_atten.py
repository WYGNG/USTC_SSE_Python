from keras.layers import Conv2D, Bidirectional, LSTM, BatchNormalization, Input, Reshape, Dense, Activation, Dropout, \
    AveragePooling2D, ZeroPadding2D, Permute, Flatten, Convolution1D, Add
from keras import Model
from keras.layers.merge import concatenate
from keras.regularizers import l2
from keras.activations import relu
import tensorflow as tf
from keras.layers.wrappers import TimeDistributed



def CRNN(img_input, nclass):
    _dropout_rate = 0
    _weight_decay = 1e-4

    _nb_filter = 64
    # conv 64 3*3 s=2
    # x = ZeroPadding2D(padding=(1, 1))(img_input)
    x = Conv2D(_nb_filter, (3, 3), strides=(1, 1), kernel_initializer='he_normal', padding='same',
               use_bias=False, kernel_regularizer=l2(_weight_decay))(img_input)

    # 64 + 4 * 8 = 96
    x, _nb_filter = dense_block(x, 8, _nb_filter, 8, None)
    # 96
    x, _nb_filter = transition_block(x, _nb_filter, _dropout_rate, stride=2, weight_decay=_weight_decay)

    # 96 + 4 * 8 = 128
    x, _nb_filter = dense_block(x, 8, _nb_filter, 8, None)
    # 128
    x, _nb_filter = transition_block(x, _nb_filter, _dropout_rate, stride=1, weight_decay=_weight_decay)

    # 128 + 4 * 8 = 160
    x, _nb_filter = dense_block(x, 8, _nb_filter, 8, None)

    x, _nb_filter = transition_block(x, _nb_filter, _dropout_rate, stride=2, weight_decay=_weight_decay)

    # 160 + 4*8 = 192
    x, _nb_filter = dense_block(x, 8, _nb_filter, 8, None)
    # 192
    x, _nb_filter = transition_block(x, _nb_filter, _dropout_rate, stride=1, weight_decay=_weight_decay)

    # 192 + 8*8 =256
    x, _nb_filter = dense_block(x, 8, _nb_filter, 8, None)
    x, _nb_filter = transition_block(x, _nb_filter, _dropout_rate, stride=2, weight_decay=_weight_decay)

    x, _nb_filter = dense_block(x, 8, _nb_filter, 8, None)
    x, _nb_filter = transition_block(x, _nb_filter, _dropout_rate, stride=1, weight_decay=_weight_decay)
    x, _nb_filter = dense_block(x, 8, _nb_filter, 8, None)
    x, _nb_filter = transition_block(x, _nb_filter, _dropout_rate, stride=2, weight_decay=_weight_decay)
    # x, _nb_filter = transition_block(x, 256, _dropout_rate, stride=2, weight_decay=_weight_decay)

    # x = Reshape((-1, 256))(x)
    x = BatchNormalization(axis=-1, epsilon=1.1e-5)(x)
    x = Activation('relu')(x)

    x = Permute((2, 1, 3), name='permute')(x)
    # x=Reshape((-1,256*3))(x)
    x = TimeDistributed(Flatten(), name='flatten')(x)

    x = Convolution1D(512, 3, activation='relu', padding='same')(x)
    # x1 = LocalSelfAttention(64, 8, mask_right=True)(x)
    # x = Add()([x,x1])
    # x = BatchNormalization(axis=-1, epsilon=1.1e-5)(x)
    x = Convolution1D(512, 3, activation='relu', padding='same')(x)
    # x = Convolution1D(512, 3, activation='relu', padding='same')(x)
    # x = Convolution1D(512, 3, activation='relu', padding='same')(x)
    x = BatchNormalization(axis=-1, epsilon=1.1e-5)(x)
    # x = Reshape([1,-1,512])(x)
    # a1 = SelfAttention(8,64)(x)
    #
    # x = Add()([a1,x])
    #
    # x = BatchNormalization(axis=-1, epsilon=1.1e-5)(x)
    #
    # a2 = SelfAttention(8, 64)(x)
    #
    # x = Add()([a2, x])
    #
    # x = BatchNormalization(axis=-1, epsilon=1.1e-5)(x)
    # x = Reshape([-1,512])(x)
    # x = Bidirectional(LSTM(256, return_sequences=True, use_bias=True,
    #                        recurrent_activation='sigmoid'))(x)
    # y_pred = Dense(nclass,activation='softmax')(x)
    # x = Bidirectional(LSTM(256, return_sequences=True, use_bias=True,
    #                        recurrent_activation='sigmoid'))(x)
    y_pred = TimeDistributed(Dense(nclass, activation='softmax'))(x)

    return y_pred


def conv_block(input, growth_rate, dropout_rate=None):
    x = BatchNormalization(axis=-1, epsilon=1.1e-5)(input)
    x = Activation('relu')(x)
    x = Conv2D(growth_rate, (3, 3), kernel_initializer='he_normal', padding='same')(x)
    if dropout_rate:
        x = Dropout(dropout_rate)(x)
    return x


def dense_block(x, nb_layers, nb_filter, growth_rate, droput_rate=None):
    for i in range(nb_layers):
        cb = conv_block(x, growth_rate, droput_rate)
        x = concatenate([x, cb], axis=-1)
        nb_filter += growth_rate
    return x, nb_filter


def transition_block(input, nb_filter, dropout_rate=None, stride=1, weight_decay=1e-4):
    x = BatchNormalization(axis=-1, epsilon=1.1e-5)(input)
    x = Activation('relu')(x)

    if stride == 2:
        x = Conv2D(nb_filter, (2, 2), strides=(2, 2), kernel_initializer='he_normal', use_bias=False, padding='same',
                   kernel_regularizer=l2(weight_decay))(x)
    elif stride == 1:
        x = Conv2D(nb_filter, (2, 2), strides=(1, 1), kernel_initializer='he_normal', use_bias=False, padding='same',
                   kernel_regularizer=l2(weight_decay))(x)

    if dropout_rate:
        x = Dropout(dropout_rate)(x)

    return x, nb_filter
