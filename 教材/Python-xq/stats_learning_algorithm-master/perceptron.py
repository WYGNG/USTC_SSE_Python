import numpy as np


class Perceptron:

    #     @staticmethod
    #     def distance_to_hyperplane(weight, bias, x):
    #         """
    #         :param weight: numpy array of hyperplane weights
    #         :param bias: numpy array of hyperplane bias
    #         :param x: features
    #         :return: scalar of distance
    #         """
    #         weight = weight.reshape(x.shape)
    #         return 1 / sqrt((weight ** 2).sum()) * abs(np.dot(weight,x) + bias)

    @staticmethod
    #损失
    def loss_function(train_feature, train_label, weight, biases):
        if train_feature.shape[1] == weight.shape[0] and train_feature.shape[0] == train_label.shape[0]:
            return - np.dot((np.matmul(train_feature, weight) + biases).flatten(), train_label.flatten())
        else:
            print(f'train_feature and weight_feature shape is {train_feature.shape[1] == weight.shape[0]}')
            print(f'train_feature and train_label shape is {train_feature.shape[1] == train_label.shape[0]}')

    @staticmethod
    def update_weight_biases(learning_rate, weight, bias, features, label):
        """
        错误分类点来更新权重和偏置
        :param learning_rate: 学习率
        :param features: 特征
        :param label: 标记
        :return:
        """
        weight_update = (weight + (learning_rate * label * features)[:, np.newaxis])
        bias_update = (bias + learning_rate * label)

        return weight_update, bias_update

    @staticmethod
    def perceptron(weight, bias, features):
        def classify(row):
            if row[0] < 0:
                return -1
            elif row[0] > 0:
                return 1
            else:
                return 0

        result = np.matmul(features, weight) + bias     #矩阵乘
        prediction = np.apply_along_axis(classify, 1, result) #维度运算得到新数组，

        return prediction #返回感知器

    def __init__(self, learning_rate=0.1, max_steps=1000):
        self.learning_rate = learning_rate
        self.steps = max_steps

    def train(self, features, label):
        weight_length = features.shape[1]  # 权重的长度获取
        bias = 0  # 偏置初始值
        weight = np.zeros(weight_length)[:, np.newaxis] #某一列零数组
        label = label[:, np.newaxis]  # 权重初始值
        error = self.loss_function(features, label, weight, bias)
        #         if error <= self.stop_error:
        #             self.weight = weight
        #             self.bias = bias
        #             self.error = error

        #         else:
        for _ in range(self.steps):
            label_hat = label.flatten() * (np.matmul(features, weight) + bias).flatten()  ## 预测
            if len(np.where(np.array(label_hat.flatten() > 0))[0]) == len(label_hat.flatten()): #where寻找符合条件的功能，即预测准确
                break

            else:
                index = np.where(np.array(label_hat.flatten() <= 0))[0]  ## 找到没预测准的数据
                wrong_result = np.random.choice(index) #随即值
                weight, bias = self.update_weight_biases(self.learning_rate,
                                                         weight,
                                                         bias,
                                                         features[wrong_result, :],
                                                         label[wrong_result])
                error = self.loss_function(features, label, weight, bias)
                if _ % 50 == 0:
                    print(f'After {_} steps, loss is {error}.')
                #                 if error <= self.stop_error:
                #                     break
                else:
                    continue
        print('Training finished.')
        self.weight = weight
        self.bias = bias
        self.error = error

    def model_parameters(self):
        return np.array([self.weight, self.bias])  

    def fit(self, features):
        return self.perceptron(self.weight, self.bias, features) 


if __name__ == '__main__':
    X = np.array([[3, 3], [4, 3], [1, 1],[2, 2]])
    Y = np.array([1, 1, -1, 1])
    perceptron = Perceptron(learning_rate=1)
    perceptron.train(X, Y)
    print(perceptron.model_parameters())
    print(perceptron.fit([[1, 1], [3, 3]]))
   # print(perceptron.model_parameters())