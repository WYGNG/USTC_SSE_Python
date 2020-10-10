import tensorflow as tf
import numpy as np
from tensorflow.python.framework.ops import convert_to_tensor

#图像加载
class ImageDataGenerator(object):
    '''
    初始化图片生成参数
    '''
    def __init__(self,dataset,mode,batch_size,num_classes=None,shuffle=False,buffer_size=1000):
        self.num_classes = num_classes
        self.mode = mode
        self.img_paths = dataset.img_path.tolist()
        self.img_ids = dataset.img_id.tolist()
        #获取数据的大小
        self.data_size = len(self.img_paths)
        if mode == "train" or mode == "val":
            self.labels = dataset.img_label.tolist()
             #打乱数据集中数据的顺序
            if shuffle:
                self._shuffle_lists()
            #将list转为tensor
            self.img_paths = convert_to_tensor(self.img_paths,dtype=tf.string)
            self.labels = convert_to_tensor(self.labels,dtype=tf.int32)
            #利用tensorflow的dataset接口创建数据集
            data = tf.data.Dataset.from_tensor_slices((self.img_paths,self.labels))
            data = data.map(self._parse_function_train,num_parallel_calls=8).prefetch(100*batch_size)
        elif mode == "test":
            self.img_paths = convert_to_tensor(self.img_paths,dtype=tf.string)
            #利用tensorflow的dataset接口创建数据集
            data = tf.data.Dataset.from_tensor_slices((self.img_paths,self.img_ids))
            data = data.map(self._parse_function_test,num_parallel_calls=8).prefetch(100*batch_size)
        else:
            raise ValueError("Invalid mode '%s'."%(self.mode))

        #打乱第一个buffer_size元素的顺序
        if shuffle:
            data = data.shuffle(buffer_size=buffer_size)

        data = data.batch(batch_size)

        self.data = data

    '''
    打乱图片路径列表和图片标签列表的顺序
    '''
    def _shuffle_lists(self):
        permutation = np.random.permutation(self.data_size)
        self.img_paths = np.array(self.img_paths)[permutation].tolist()
        self.labels = np.array(self.labels)[permutation].tolist()

    def _parse_function_train(self,filename,label):
        #标签转为one-hot编码
        one_hot = tf.one_hot(label,self.num_classes)
        #加载图片的预处理
        img_string = tf.read_file(filename)
        img_decode = tf.image.decode_jpeg(img_string,channels=3)
        img_resized = tf.image.resize_images(img_decode,[227,227])
        return img_resized,one_hot

    def _parse_function_test(self,filename,img_ids):
        #加载图片的预处理
        img_string = tf.read_file(filename)
        img_decode = tf.image.decode_jpeg(img_string,channels=3)
        img_resized = tf.image.resize_images(img_decode,[227,227])
        return img_resized,img_ids
