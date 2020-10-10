import os

#设置txt保存目录
save_txt_dir = "txt"

def generate_txt(save_mode,train_img_dir):
    '''将图片的id和标签信息写入到txt中
    :param save_mode: train or test
    :param train_img_dir: 图片所在的目录
    :return: 空
    '''
    if save_mode not in ["train","test"]:
        raise ValueError("save_mode:%s,is train or test"%save_mode)
    # 判断生成目录
    if not os.path.exists(train_img_dir):
        raise ValueError("train_img_dir:%s,is not exist"%train_img_dir)

    if not os.path.isdir(train_img_dir):
        raise ValueError("train_img_dir:%s,is not directory"%train_img_dir)
    if not os.path.exists(save_txt_dir):
        os.makedirs(save_txt_dir)
    if save_mode == "train":
        save_txt_path = os.path.join(save_txt_dir,"train.txt")
    else:
        save_txt_path = os.path.join(save_txt_dir,"test.txt")
    #文件操作
    with open(save_txt_path,mode="w",encoding="utf-8") as f_wirter:
        for img_name in os.listdir(train_img_dir):
            img_path = os.path.join(train_img_dir,img_name).replace("\\","/")
            if img_path.endswith("jpg"):
                if save_mode == "train":
                    #获取图片的标签名cat或者dog
                    label_name,img_id,_ = img_name.split(".")
                    #将图片信息写入到txt文件中,使用逗号进行分割
                    f_wirter.write("%s,%s,%s\n"%(img_id,img_path,label_name))
                else:
                    #获取图像的id
                    img_id,_ = img_name.split(".")
                    #写入文件，图像的id和路径
                    f_wirter.write("%s,%s\n"%(img_id,img_path))
        f_wirter.close()

if __name__ == "__main__":
    #将训练集图片保存为txt文件
    generate_txt("train","D:/pythonwork/pro/data/train/train")
    #将测试集图片保存为txt文件
    generate_txt("test","D:/pythonwork/pro/data/test/test")
