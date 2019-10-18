import numpy as np


class naivebayes:

    @staticmethod
    def unique_prob(arr, label_nums=1):
        unique, count = np.unique(arr, return_counts=True)
        return unique, count / label_nums, dict(zip(list(unique), list(count)))

    @staticmethod
    def unique_to_dict(unique, cor_prob):
        unique = list(unique)
        cor_prob = list(cor_prob)
        dict = {}
        for i in range(len(unique)):
            dict[unique[i]] = cor_prob[i]
        return dict

    def __init__(self, lam=1, S=1):
        self.lam = lam
        self.S = S

    def train(self, features, labels):
        label_unique, label_prob, label_count = nb.unique_prob(labels, len(labels))
        label_p = self.unique_to_dict(label_unique, label_prob)
        concat = np.hstack((features, labels[:, np.newaxis]))
        prob_feature = []
        for i in label_unique:
            feature_label_p = []
            concat_ = concat[(concat[:, -1] == i), :]
            for j in concat_.T[:-1]:
                unique, count_prob, _ = self.unique_prob(j, label_count[i])
                feature_label_p.append(self.unique_to_dict(unique, count_prob))
            prob_feature.append(feature_label_p)

        self.labels_prob = label_p
        self.labels = label_unique
        self.features_prob = prob_feature

    def fit(self, features):

        def pred_row(row):
            pred = []
            for t, j in enumerate(self.labels):
                pred_ = self.labels_prob[j]
                a = []
                a.append(pred_)
                for i, k in enumerate(row):
                    try:
                        feature = self.features_prob[t][i][k]
                    except:
                        feature = 0
                    a.append(feature)
                pred_array = np.array(a)
                final = np.multiply.reduce(pred_array)
                pred.append(final)
            return self.labels[np.argmax(np.array(pred))]

        return np.apply_along_axis(pred_row, 1, features)

if __name__ == '__main__':

    X = np.array([[3, 3], [4, 3], [1, 1]])
    Y = np.array([1, 1, -1])
    nb = naivebayes()
    nb.train(X, Y)
    print(nb.fit([[4, 3], [3, 3]]))






