
import numpy as np
import treelib as tl ## 需要进一步考察是否真的需要用这个方法

def information_gain(feature, labels):
    """
    :type labels: 1-D numpy array
    :type feature: 1-D numpy array
    """
    labels_unique, labels_count = np.unique(labels, return_counts=True)
    base_cal = labels_count / len(labels)
    emprical_entropy_label = - np.sum(base_cal * np.log2(base_cal))
    #print(emprical_entropy_label)
    feature_label = np.hstack((feature[:, np.newaxis], labels[:, np.newaxis]))
    #print(feature_label)
    feature_entropy = []
    feature_unique, feature_count = np.unique(feature, return_counts = True)
    for j in feature_unique:
        feature_label_ = feature_label[(feature_label[:, 0] == j), :]
        #print(feature_label_)
        label_ = len(feature_label_[:,1].T)
        #print(label_)
        final_unique, final_count = np.unique(feature_label_[:,1].T, return_counts=True)
        #print(final_unique, final_count)
        feature_cal = final_count / label_
        #print(feature_cal)
        emprical_entropy_feature = - np.sum(feature_cal * np.log2(feature_cal)) * (label_ /len(labels))
        #print(emprical_entropy_feature)
        feature_entropy.append(emprical_entropy_feature)
        #print(feature_entropy)
    return emprical_entropy_label - np.sum(np.array(feature_entropy))


def information_gain_ratio(feature, labels):
    """
    :type labels: 1-D numpy array
    :type feature: 1-D numpy array
    """
    labels_unique, labels_count = np.unique(labels, return_counts=True)
    base_cal = labels_count / len(labels)
    emprical_entropy_label = - np.sum(base_cal * np.log2(base_cal))
    #print(emprical_entropy_label)
    feature_label = np.hstack((feature[:, np.newaxis], labels[:, np.newaxis]))
    #print(feature_label)
    feature_entropy = []
    feature_label_entropy = []
    feature_unique, feature_count = np.unique(feature, return_counts = True)
    for j in feature_unique:
        feature_label_ = feature_label[(feature_label[:, 0] == j), :]
        #print(feature_label_)
        label_ = len(feature_label_[:,1].T)
        feature_label_entropy.append(label_)
        #print(label_)
        final_unique, final_count = np.unique(feature_label_[:,1].T, return_counts=True)
        #print(final_unique, final_count)
        feature_cal = final_count / label_
        #print(feature_cal)
        emprical_entropy_feature = - np.sum(feature_cal * np.log2(feature_cal)) * (label_ /len(labels))
        #print(emprical_entropy_feature)
        feature_entropy.append(emprical_entropy_feature)
        #print(feature_entropy)
    feature_label_entropy = -np.sum(np.array(feature_label_entropy) / len(labels) * np.log2(np.array(feature_label_entropy) / len(labels)))
    return (emprical_entropy_label - np.sum(np.array(feature_entropy)))/ feature_label_entropy


def subset_split(features, labels, feature_A_col):
    """
    :param features: features columns
    :param labels: label column
    :param feature_A_col: the column position of feature A
    :return:
    """
    feature_label = np.hstack((features, labels[:, np.newaxis]))
    feature_unique, feature_count = np.unique(features[:,feature_A_col], return_counts=True)
    subset = []
    for j in feature_unique:
        feature_label_ = feature_label[(feature_label[:, feature_A_col] == j), :]
        subset.append(feature_label_)
    return [np.delete(np.array(i), feature_A_col, 1) for i in subset]


a = np.array([[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],[0,0,1,1,0,0,0,1,0,0,0,0,1,1,0],[0,0,0,1,0,0,0,1,1,1,1,1,0,0,0],[0,1,1,0,0,0,1,1,2,2,2,1,1,2,0]])
#a = np.array([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3])
b = np.array([0,0,1,1,0,0,0,1,1,1,1,1,1,1,0])

class DecisionTreeClassifier:

    @staticmethod
    def information_gain(feature, labels):
        """
        :type labels: 1-D numpy array
        :type feature: 1-D numpy array
        """
        labels_unique, labels_count = np.unique(labels, return_counts=True)
        base_cal = labels_count / len(labels)
        emprical_entropy_label = - np.sum(base_cal * np.log2(base_cal))
        # print(emprical_entropy_label)
        feature_label = np.hstack((feature[:, np.newaxis], labels[:, np.newaxis]))
        # print(feature_label)
        feature_entropy = []
        feature_unique, feature_count = np.unique(feature, return_counts=True)
        for j in feature_unique:
            feature_label_ = feature_label[(feature_label[:, 0] == j), :]
            # print(feature_label_)
            label_ = len(feature_label_[:, 1].T)
            # print(label_)
            final_unique, final_count = np.unique(feature_label_[:, 1].T, return_counts=True)
            # print(final_unique, final_count)
            feature_cal = final_count / label_
            # print(feature_cal)
            emprical_entropy_feature = - np.sum(feature_cal * np.log2(feature_cal)) * (label_ / len(labels))
            # print(emprical_entropy_feature)
            feature_entropy.append(emprical_entropy_feature)
            # print(feature_entropy)
        return emprical_entropy_label - np.sum(np.array(feature_entropy))

    @staticmethod
    def information_gain_ratio(feature, labels):
        """
        :type labels: 1-D numpy array
        :type feature: 1-D numpy array
        """
        labels_unique, labels_count = np.unique(labels, return_counts=True)
        base_cal = labels_count / len(labels)
        emprical_entropy_label = - np.sum(base_cal * np.log2(base_cal))
        # print(emprical_entropy_label)
        feature_label = np.hstack((feature[:, np.newaxis], labels[:, np.newaxis]))
        # print(feature_label)
        feature_entropy = []
        feature_label_entropy = []
        feature_unique, feature_count = np.unique(feature, return_counts=True)
        for j in feature_unique:
            feature_label_ = feature_label[(feature_label[:, 0] == j), :]
            # print(feature_label_)
            label_ = len(feature_label_[:, 1].T)
            feature_label_entropy.append(label_)
            # print(label_)
            final_unique, final_count = np.unique(feature_label_[:, 1].T, return_counts=True)
            # print(final_unique, final_count)
            feature_cal = final_count / label_
            # print(feature_cal)
            emprical_entropy_feature = - np.sum(feature_cal * np.log2(feature_cal)) * (label_ / len(labels))
            # print(emprical_entropy_feature)
            feature_entropy.append(emprical_entropy_feature)
            # print(feature_entropy)
        feature_label_entropy = -np.sum(
            np.array(feature_label_entropy) / len(labels) * np.log2(np.array(feature_label_entropy) / len(labels)))
        return (emprical_entropy_label - np.sum(np.array(feature_entropy))) / feature_label_entropy

    def __init__(self):
        pass


    def train(self, features, labels):
        decision_tree = tl.tree()
        if len(np.unique(labels)[0]) == 1:
            return decision_tree.create_node(str(labels[0]), 'label') ## root_node
        if


        pass

    def fit(self):
        pass


tl.
