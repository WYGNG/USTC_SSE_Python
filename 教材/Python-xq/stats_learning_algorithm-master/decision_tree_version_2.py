import numpy as np


# import treelib as tl ## 需要进一步考察是否真的需要用这个方法


class TreeNode:  ## 决策树结点构造,通过字典的方法来表示

    def __init__(self, feature_name=None, value=None, parent_node={}, sub_tree={}, relation=None):
        self.value = value
        self.parent_node = parent_node  ## dictionary (key是节点对应的特征值，value对应的是具体的特征)
        self.sub_tree = sub_tree
        self.feature_name = feature_name
        self.relation = relation

    def add_subtree(self, subtree_root_node):
        if isinstance(subtree_root_node, TreeNode) == True:
            self.node_name().update(subtree_root_node.node_name())
        else:
            self.node_name().update(subtree_root_node)

    def node_name(self):
        return {self.feature_name: self.sub_tree}

    def attach_to_node(self, parent_node):
        self.parent_node = parent_node






class Tree:  ## 决策树构造，根结点，节点traverse

    def __init__(self, root_node=TreeNode()):
        self.root_node = root_node


def information_gain(feature, labels):  ##信息增益
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


def information_gain_ratio(feature, labels): ## 信息增益率
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


def subset_split(features, labels, feature_A_col): ## 按照特征把数据集分为几个subset
    """
    :param features: features columns
    :param labels: label column
    :param feature_A_col: the column position of feature A
    :return: all subset obtained after tree split based on feature A
    """
    feature_label = np.hstack((features, labels[:, np.newaxis]))
    feature_unique, feature_count = np.unique(features[:, feature_A_col], return_counts=True)
    subset = []
    for j in feature_unique:
        feature_label_ = feature_label[(feature_label[:, feature_A_col] == j), :]
        subset.append(feature_label_)
    return dict(zip(list(feature_unique),[np.delete(np.array(i), feature_A_col, 1) for i in subset]))




def ID3(dataset_features, dataset_labels, feature_names, epislon=0):
    feature_shape = dataset_features.shape
    feature_names_dict = dict(zip(range(feature_shape[1]), feature_names))
    if len(np.unique(dataset_labels)) == 1:
        #root_node = TreeNode(feature_name='label', value=dataset_labels[0], sub_tree=dataset_labels[0])
        #print(root_node.node_name())
        #print('got to!')
        return dataset_labels[0]
        #return root_node
    # decision_tree = Tree(root_node, is_root=True)

    elif feature_shape[1] == 0:
        (value, counts) = np.unique(dataset_labels, return_counts=True)
        index = np.argmax(counts)
        print('yes')
        #root_node = TreeNode(feature_name='label', value=value[index], sub_tree=value[index])
        #print(root_node.node_name())
        return value[index]

    else:
    ### 找到entropy增加最大的特征
        information_gain_entropy = [information_gain(dataset_features[:, i], dataset_labels) for i in range(feature_shape[1])]
        if max(information_gain_entropy) <= epislon:
            (value, counts) = np.unique(dataset_labels, return_counts=True)
            index = np.argmax(counts)
            #root_node = TreeNode(feature_name='label', value=value[index], sub_tree=value[index])
            return value[index]

        else:
            max_entropy_gain_col_num = np.argmax(np.array(information_gain_entropy))
            max_entropy_feature = feature_names_dict[max_entropy_gain_col_num]
            root_node = TreeNode(feature_name=max_entropy_feature)
            #print(root_node.node_name())
            tree = {max_entropy_feature:{}}
            del(feature_names[max_entropy_gain_col_num])
            #unique_values_feature = np.unique(dataset_features[:,max_entropy_gain_col_num])
            #feature_names.remove(max_entropy_feature)
            print('______________________________________________')
            print(subset_split(dataset_features, dataset_labels, max_entropy_gain_col_num))
            print('_______________________________________________')
            for unique_values_feature, subset in subset_split(dataset_features, dataset_labels, max_entropy_gain_col_num).items():
                print(subset)
                print(unique_values_feature)
                subset_features = subset[:, :-1]
                print(subset_features)
                subset_labels = subset[:, -1].flatten()
                print(subset_labels)
                print(max_entropy_feature)
                subtree_ = ID3(subset_features, subset_labels, feature_names)
                tree[max_entropy_feature][unique_values_feature] = subtree_
                #root_node.sub_tree[unique_values_feature]=subtree_
                #for i in np.unique(subset_labels):
                    #root_node.sub_tree[max_entropy_feature][i] = ID3(subset_features, subset_labels, feature_names).node_name()
                    #tree[max_entropy_feature][i]= ID3(subset_features, subset_labels, feature_names)
                #tree[max_entropy_feature][subset_labels[0]]=ID3(subset_features, subset_labels, feature_names)
            return tree

def C45(dataset_features, dataset_labels, feature_names, epislon=0):
    feature_shape = dataset_features.shape
    feature_names_dict = dict(zip(range(feature_shape[1]), feature_names))
    if len(np.unique(dataset_labels)) == 1:
        root_node = TreeNode(feature_name='label', value=np.unique(dataset_labels)[0])
        return np.unique(dataset_labels)[0]
    # decision_tree = Tree(root_node, is_root=True)

    elif feature_shape[1] == 0:
        (value, counts) = np.unique(dataset_labels, return_counts=True)
        index = np.argmax(counts)
        root_node = TreeNode(feature_name='label', value=value[index])
        return value[index]

    else:
    ### 找到entropy增加最大的特征
        information_gain_entropy = [information_gain_ratio(dataset_features[:, i], dataset_labels) for i in range(feature_shape[1])]
        if max(information_gain_entropy) <= epislon:
            (value, counts) = np.unique(dataset_labels, return_counts=True)
            index = np.argmax(counts)
            root_node = TreeNode(feature_name='label', value=value[index])
            return value[index]

        else:
            max_entropy_gain_col_num = np.argmax(np.array(information_gain_entropy))
            max_entropy_feature = feature_names_dict[max_entropy_gain_col_num]
            root_node = TreeNode(feature_name=max_entropy_feature)
            feature_names.remove(max_entropy_feature)
            tree = {max_entropy_feature:{}}
            for value, subset in subset_split(dataset_features, dataset_labels, max_entropy_gain_col_num).items():
                subset_features = subset[:, :-1]
                subset_labels = subset[:, -1]
                subtree = C45(subset_features, subset_labels, feature_names)
                tree[max_entropy_feature][value] = subtree
                #root_node.add_subtree(C45(subset_features, subset_labels, feature_names))
        return tree





a = np.array([[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3], [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 1, 1, 2, 2, 2, 1, 1, 2, 0]])
# a = np.array([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3])
b = np.array([0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0])


print(C45(a.T,b,feature_names = ['age','is_working','has_house','credit_history']))



