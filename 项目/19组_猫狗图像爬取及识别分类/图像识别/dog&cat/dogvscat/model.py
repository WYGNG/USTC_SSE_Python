from keras import callbacks
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.models import Sequential,load_model
from keras.layers import Conv2D,MaxPool2D,Dropout,Flatten,Dense
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator,img_to_array,load_img
from tkinter.filedialog import askopenfilename
import os

# 注意：除test（）外所有路径均仅为限于本模块使用的相对路径

SHAPE=[224,224]

# 使用去除Dense层的预训练的VGG-16模型加上自己定义的Dense层（2层：256+2）进行训练
# 返回定义好的模型model用于训练
def vgg():
    VGG16_model = VGG16(weights='imagenet',include_top=False, input_shape=(SHAPE[0],SHAPE[1],3))
    VGG16_model.trainable=False
    # 自定义Dense层
    top_model=Sequential()
    top_model.add(Flatten(input_shape=VGG16_model.output_shape[1:]))
    top_model.add(Dense(256,activation='relu'))
    top_model.add(Dropout(0.5))
    top_model.add(Dense(2,activation='softmax'))
    # 将VGG与自定义层结合起来
    model=Sequential()
    model.add(VGG16_model)
    model.add(top_model)
    model.summary()
    return model

# vgg()
# 自定义的CNN，效果一般，准确率在0.7左右
def cnn_diy():
    model=Sequential()
    model.add(Conv2D(64,kernel_size=(3,3),strides=(1,1),padding='same',input_shape=(SHAPE[0],SHAPE[1],3),activation='relu'))
    model.add(MaxPool2D((2,2)))
    model.add(Conv2D(64, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(MaxPool2D((2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(MaxPool2D((2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(MaxPool2D((2, 2)))
    model.add(Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(MaxPool2D((2, 2)))
    model.add(Conv2D(256, kernel_size=(3, 3), strides=(1, 1), padding='same', activation='relu'))
    model.add(MaxPool2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(512,activation='relu'))
    model.add(Dense(2,activation='softmax'))
    return model

# 使用生成器获取训练数据，减少内存占用
# 返回
def get_data():
    # train_path 训练数据路径母文件夹，该文件夹下存放两个分类的文件夹
    train_path = 'train'
    val_path='val'
    # 数据增强方案
    # train_datagen=ImageDataGenerator(rotation_range=40,
    #                                  height_shift_range=0.1,
    #                                  width_shift_range=0.1,
    #                                  horizontal_flip=True,shear_range = 20,
    #                                  zoom_range = 0.2,rescale=1./255,
    #                                  data_format='channels_last')
    train_datagen=ImageDataGenerator(rescale=1/255)
    val_datagen = ImageDataGenerator(rescale = 1/255)

    # 此方法直接识别train_path下分类并打标签
    train_generator=train_datagen.flow_from_directory(train_path,target_size=(SHAPE[0],SHAPE[1]),
                                                      class_mode='categorical',
                                                      batch_size=128,
                                                      shuffle=True)
    val_generator=val_datagen.flow_from_directory(val_path,target_size=(SHAPE[0],SHAPE[1]),
                                                  batch_size=128,
                                                  class_mode='categorical')
    return train_generator,val_generator

# 训练模型
def train():
    train_generator, val_generator = get_data()
    model=vgg()
    model.compile(optimizer=RMSprop(lr=1e-4),loss='categorical_crossentropy',metrics=['accuracy'])
    cbk=callbacks.ModelCheckpoint('bestModelVgg.hdf5',save_best_only=True)
    history=model.fit_generator(train_generator,steps_per_epoch=64,epochs=30,callbacks=[cbk],
                                validation_data=val_generator,validation_steps=16)


# 测试传入图片是猫还是狗
# img_path：图片路径
# dorc：“猫”或“狗”
def test(img_path):
    label=np.array(['猫','狗'])
    model=load_model('dogvscat/bestModelVgg.hdf5')
    img=load_img(img_path)
    img=img.resize((SHAPE[0],SHAPE[1]))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,0)
    #print(label[model.predict_classes(img)])
    dorc=label[(model.predict_classes(img))[0]]
    return dorc

# 加载训练好的模型，使用猫狗各一百张进行预测并计算准确率
# 返回准确率acc
def evaluate():
    label = np.array(['猫', '狗'])
    model = load_model('bestModelVgg.hdf5')
    test_1_path_cat = 'test_1/cat/'
    test_1_path_dog = 'test_1/dog/'
    dirs=os.listdir(test_1_path_cat)
    acc=0
    k=0
    j=1
    for path in [test_1_path_cat,test_1_path_dog]:
        dirs = os.listdir(path)
        for file in dirs:
            img = load_img(path+file)
            img = img.resize((SHAPE[0],SHAPE[1]))
            img = img_to_array(img)
            img = img / 255
            img = np.expand_dims(img, 0)
            print(j)
            j+=1
            print(label[model.predict_classes(img)])
            if(model.predict_classes(img)==k):
                acc+=1
        k=1
    acc/=2000
    return acc


if __name__ == '__main__':
    #train()
    #img_path=askopenfilename()
    #dorc=test(img_path)
    #print(dorc)
    #acc=evaluate()
    #print(acc)
    vgg()
