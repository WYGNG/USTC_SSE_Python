from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.layers import Dense, Dropout
from keras.models import Model
from keras.optimizers import Adam, SGD
from keras.preprocessing.image import ImageDataGenerator, image
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from keras import backend as K
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFile, Image, ImageEnhance
import pandas as pd
import os
import cv2
import random
import itertools

ImageFile.LOAD_TRUNCATED_IMAGE = True

TRAIN_PATH = './input/training/training/'
VALID_PATH = './input/validation/validation/'
TEST_PATH = './input/test/test/'
MODEL_CHECK_WEIGHT_NAME = 'resnet_monkey.h5'


class train_model(object):
    def __init__(self):
        self.labels = ['mantled_howler', 'patas_monkey', 'bald_uakari', 'japanese_macaque', 'pygmy_marmoset',
                       'white_headed_capuchin', 'silvery_marmoset', 'common_squirrel_monkey',
                       'black_headed_night_monkey',
                       'nilgiri_langur', ]

    def get_datagen(self, flag=[False, False, False]):
        datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
        traingen = None
        validgen = None
        testgen = None
        if flag[0] == True:
            traingen = datagen.flow_from_directory(TRAIN_PATH, target_size=(224, 224), batch_size=64,
                                                   class_mode='categorical')
        if flag[1] == True:
            validgen = datagen.flow_from_directory(VALID_PATH, target_size=(224, 224), batch_size=16,
                                                   class_mode='categorical', shuffle=False)
        if flag[2] == True:
            testgen = datagen.flow_from_directory(TEST_PATH, target_size=(224, 224), batch_size=16,
                                                  class_mode='categorical', shuffle=False)

        return traingen, validgen, testgen

    def model(self):
        K.set_learning_phase(0)
        model = ResNet50(input_shape=(224, 224, 3), include_top=False, weights='imagenet', pooling='avg')
        K.set_learning_phase(1)
        x = model.output
        x = Dense(512, activation='relu')(x)
        x = Dropout(0.5)(x)
        x = Dense(512, activation='relu')(x)
        x = Dropout(0.5)(x)
        output = Dense(len(self.labels), activation='softmax', name='custom_output')(x)
        custom_resnet = Model(inputs=model.input, outputs=output)

        for layer in model.layers:
            layer.trainable = False

        custom_resnet.compile(Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
        # custom_resnet.summary()
        return custom_resnet

    def train(self):
        custom_resnet = self.model()
        traingen, validgen, _ = self.get_datagen()
        es_callback = EarlyStopping(monitor='val_acc', patience=5, mode='max')
        mc_callback = ModelCheckpoint(filepath=MODEL_CHECK_WEIGHT_NAME, monitor='val_acc', save_best_only=True,
                                      mode='max')
        train_history = custom_resnet.fit_generator(traingen, steps_per_epoch=len(traingen), epochs=5,
                                                    validation_data=validgen, validation_steps=len(validgen),
                                                    verbose=1,
                                                    callbacks=[es_callback, mc_callback])
        return train_history

    # 画学习曲线
    def show_learncourve(self, train_history):
        plt.figure(1)
        plt.subplot(221)
        plt.plot(train_history.history['acc'])
        plt.plot(train_history.history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train accuracy', 'validation accuracy'])

        plt.subplot(222)
        plt.plot(train_history.history['loss'])
        plt.plot(train_history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epochs')
        plt.legend(['train loss', 'validation loss'])
        plt.show()

    # 画混淆矩阵
    def plot_confusion_matrix(self, cm, target_names, title='Confusion matrix', cmap=None, normalize=False):
        accuracy = np.trace(cm) / float(np.sum(cm))
        misclass = 1 - accuracy
        if cmap is None:
            cmap = plt.get_cmap('Blues')
        plt.figure(figsize=(10, 8))
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()

        if target_names is not None:
            tick_marks = np.arange(len(target_names))
            plt.xticks(tick_marks, target_names, rotation=45)
            plt.yticks(tick_marks, target_names)

        if normalize:
            cm = cm.astype('float32') / cm.sum(axis=1)
            cm = np.round(cm, 2)

        thresh = cm.max() / 1.5 if normalize else cm.max() / 2
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            if normalize:
                plt.text(j, i, "{:0.2f}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")
            else:
                plt.text(j, i, "{:,}".format(cm[i, j]),
                         horizontalalignment="center",
                         color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel("Predicted label\naccuracy={:0.4f}\n misclass={:0.4f}".format(accuracy, misclass))
        plt.show()

    # 加载模型
    def load_model(self, model_path=MODEL_CHECK_WEIGHT_NAME):
        custom_resnet = self.model()
        custom_resnet.load_weights(model_path)
        return custom_resnet

    # 预测一批数据
    def predict_generator(self, testgen, model=None):
        if model is None:
            model = self.load_model()
        predict = model.predict_generator(testgen, steps=len(testgen), verbose=1)
        return predict

    # 预测一个指定数据
    def predict(self, images, model=None):
        if model is None:
            model = self.load_model()
        predict = model.predict(images)
        return predict


if __name__ == '__main__':
    _, _, testgen = train_model().get_datagen(flag=[False, False, True])

    result = train_model().predict_generator(testgen)
    print(result)
