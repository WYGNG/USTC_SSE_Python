import numpy as np
from scipy.spatial import KDTree

class KNN:

    @staticmethod
    def distance_calc(x, y, norm = 2):
        return np.linalg.norm(x-y, ord = norm)


    def __init__(self, K=2, distance_norm=2):
        self.K = K
        self.distance_norm = distance_norm

    def train(self, features, labels):
        tree = KDTree(features)
        self.tree = tree
        self.features = features
        self.labels = labels[:,np.newaxis]

    def get_labels(self, features):
        labels = self.labels[(self.tree.query(features, k=self.K, p=self.distance_norm))[1]]
        unique, counts = np.unique(labels.flatten(), return_counts=True)
        pred_label = unique[np.where(counts == counts.max())[0][0]]
        return pred_label


    def fit(self, features):
        return np.apply_along_axis(self.get_labels, axis = 1, arr = features)

if __name__ == '__main__':
    X = np.array([[3, 3], [4, 3], [1, 1]])
    Y = np.array([1, 1, -1])
    knn = KNN(K=1, distance_norm=1)
    knn.train(X, Y)
    print(knn.get_labels([1,2]))
    print(knn.fit([[0, 0], [600, 32],[3, 9]]))











