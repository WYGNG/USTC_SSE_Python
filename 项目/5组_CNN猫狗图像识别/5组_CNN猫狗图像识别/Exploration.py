import matplotlib.pyplot as plt
#解决显示中文乱码问题
plt.rcParams["font.sans-serif"]=["SimHei"]
import seaborn as sns
import numpy as np
from PIL import Image
from sklearn.metrics import confusion_matrix,classification_report
from util_data import get_img_infos,split_dataset
sns.set_style("white")

def plot_label_distribution(img_labels):
    #绘制猫和狗的分布
    sns.countplot(img_labels)
    plt.title("cat and dog distribution")
    plt.show()

#用来绘制验证集和测试集的类标分布
def val_pred_and_real_distribution(pred_labels,real_labels):
    label_num_to_name = {0:"cat",1:"dog"}
    #将数字标签转为文字标签
    pred_labels = [label_num_to_name[label] for label in pred_labels]
    real_labels = [label_num_to_name[label] for label in real_labels]
    plt.figure(22)
    #绘制预测结果和真实结果标签的分布情况
    plt.subplot(221)
    sns.countplot(pred_labels)
    plt.title("prediction label distribution")
    plt.subplot(222)
    sns.countplot(real_labels)
    plt.title("real label distribution")
    #绘制预测正确结果和预测错误结果的分布情况
    #计算预测正确的下标位置
    correct_index = np.array(pred_labels)==np.array(real_labels)
    correct = np.array(real_labels)[correct_index]
    plt.subplot(223)
    sns.countplot(correct)
    plt.title("prediction correct label distribution")
    #计算预测错误的下标位置
    error_index = np.array(pred_labels) != np.array(real_labels)
    error = np.array(real_labels)[error_index]
    plt.subplot(224)
    sns.countplot(error)
    plt.title("prediction error label distribution")
    plt.show()

#展示预测正确和错误标签的部分图片
def show_part_image(pred_labels,real_labels,img_paths):
    label_num_to_name = {0:"cat",1:"dog"}
    #获取预测正确的下标
    correct_index = np.array(pred_labels) == np.array(real_labels)
    correct_pred_labels = np.array(pred_labels)[correct_index]
    correct_real_labels = np.array(real_labels)[correct_index]
    correct_img_paths = np.array(img_paths)[correct_index]
    #获取预测错误的下标
    error_index = np.array(pred_labels) != np.array(real_labels)
    error_pred_labels = np.array(pred_labels)[error_index]
    error_real_labels = np.array(real_labels)[error_index]
    error_img_paths = np.array(img_paths)[error_index]
    #展示十张图片上面5张预测正确的图片,下面5张预测错误的图片
    plt.figure(25)
    for i in range(5):
        plt.subplot(2,5,i+1)
        plt.imshow(Image.open(correct_img_paths[i]))
        plt.title("预测:%s\n真实:%s"%(label_num_to_name[correct_pred_labels[i]],
                                           label_num_to_name[correct_real_labels[i]]))
        plt.subplot(2,5,i+6)
        plt.imshow(Image.open(error_img_paths[i]))
        plt.title("预测:%s\n真实:%s"%(label_num_to_name[error_pred_labels[i]],
                                           label_num_to_name[error_real_labels[i]]))
    plt.show()

#绘制混淆矩阵,输出分类情况报告
def classifiction_report_info(pred_labels,real_labels):
    #输出分类结果报告
    classification_info = classification_report(real_labels,pred_labels,target_names=["cat","dog"])
    print(classification_info)
    #展示混淆矩阵
    con_matrix = confusion_matrix(real_labels,pred_labels)
    sns.heatmap(con_matrix,annot=True)
    plt.show()

if __name__ == "__main__":
    img_ids,img_labels,img_paths = get_img_infos("train","txt/train.txt")
    train_dataset,val_dataset = split_dataset(img_ids,img_paths,img_labels)
    print(img_paths)
    plot_label_distribution(train_dataset["img_label"])
    plot_label_distribution(val_dataset["img_label"])
