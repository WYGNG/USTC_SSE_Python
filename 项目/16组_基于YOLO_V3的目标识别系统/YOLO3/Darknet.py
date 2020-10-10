from __future__ import division
from Parse_config import parse_config
from Parse_config import create_modules

from util import *


class Darknet(nn.Module):
    def __init__(self, cgfile):
        super(Darknet, self).__init__()
        self.blocks = parse_config(cgfile)
        self.net_info, self.module_list = create_modules(self.blocks)

    # 定义前向传播,self.blocks因为的第一个元素self.blocks是一个net不属于正向传递的块。
    def forward(self, x, CUDA):
        modules = self.blocks[1:]

        # 键值对。key为layer的索引，value是特征矩阵（feature map）
        outputs = {}
        # 写标志为0
        write = 0
        for i, module in enumerate(modules):
            module_type = module['type']
            if module_type == 'convolutional' or module_type == 'upsample':
                # 如果模块是卷积模块或上采样模块，则这就是正向传递的工作方式。
                x = self.module_list[i](x)


            elif module_type == 'route':
                layers = module['layers']
                layers = [int(a) for a in layers]

                if layers[0] > 0:
                    layers[0] = layers[0] - i

                if len(layers) == 1:
                    x = outputs[i + layers[0]]

                else:
                    if (layers[1]):
                        layers[1] = layers[1] - i

                    mp1 = outputs[i + layers[0]]
                    mp2 = outputs[i + layers[1]]

                    # 在深度上连接，及channels连接，要保证长宽一致
                    x = torch.cat((mp1, mp2), 1)

                    # 残差网络
            elif module_type == 'shortcut':
                from_ = int(module['from'])
                x = outputs[i - 1] + outputs[i + from_]

            elif module_type == 'yolo':

                #获得三个anchors值
                anchors = self.module_list[i][0].anchors
                # 获得输入维度
                input_dim = int(self.net_info['height'])
                # 需要检测的物体个数
                num_classes = int(module['classes'])

                # transform
                x = x.data.cuda()
                #x的shape(batch_size,channels,长，宽)
                #shape torch.Size([1, 255, 13, 13])
                #print('prediction.shape',x.shape)
                x = predict_transform(x, input_dim, anchors, num_classes, CUDA)
                # 第一次yolo检测的时候，因为第二张检测图还没生成，还不能concat
                if not write:  # if no collector has been intialised.
                    detections = x
                    write = 1
                else:
                    detections = torch.cat((detections, x), 1)

            outputs[i] = x
        # 返回的是三张特征图的连接
        return detections

    def load_weights(self, weightfile):

        # 打开权重文件
        fp = open(weightfile, "rb")

        # The first 4 values are header information
        # 1. Major version number
        # 2. Minor Version Number
        # 3. Subversion number 
        # 4. IMages seen 
        header = np.fromfile(fp, dtype=np.int32, count=5)
        self.header = torch.from_numpy(header)
        self.seen = self.header[3]

        # The rest of the values are the weights
        # Let's load them up
        weights = np.fromfile(fp, dtype=np.float32)

        ptr = 0
        for i in range(len(self.module_list)):
            module_type = self.blocks[i + 1]["type"]

            if module_type == "convolutional":
                model = self.module_list[i]
                try:
                    batch_normalize = int(self.blocks[i + 1]["batch_normalize"])
                except:
                    batch_normalize = 0

                conv = model[0]

                if (batch_normalize):
                    bn = model[1]

                    # 获得批量归一化层的参数个数
                    num_bn_biases = bn.bias.numel()

                    # 从weights中加载参数
                    bn_biases = torch.from_numpy(weights[ptr:ptr + num_bn_biases])
                    ptr += num_bn_biases

                    bn_weights = torch.from_numpy(weights[ptr: ptr + num_bn_biases])
                    ptr += num_bn_biases

                    bn_running_mean = torch.from_numpy(weights[ptr: ptr + num_bn_biases])
                    ptr += num_bn_biases

                    bn_running_var = torch.from_numpy(weights[ptr: ptr + num_bn_biases])
                    ptr += num_bn_biases

                    # 把权重reshape成模型需要的参数的形状
                    bn_biases = bn_biases.view_as(bn.bias.data)
                    bn_weights = bn_weights.view_as(bn.weight.data)
                    bn_running_mean = bn_running_mean.view_as(bn.running_mean)
                    bn_running_var = bn_running_var.view_as(bn.running_var)

                    # 复制参数到模型中去
                    bn.bias.data.copy_(bn_biases)
                    bn.weight.data.copy_(bn_weights)
                    bn.running_mean.copy_(bn_running_mean)
                    bn.running_var.copy_(bn_running_var)

                else:
                    # 如果没加载成功，获得卷积偏差参数的数量
                    num_biases = conv.bias.numel()

                    # 加载权重
                    conv_biases = torch.from_numpy(weights[ptr: ptr + num_biases])
                    ptr = ptr + num_biases

                    # 把权重reshape成模型需要的参数的形状
                    conv_biases = conv_biases.view_as(conv.bias.data)

                    # 复制参数到模型中去
                    conv.bias.data.copy_(conv_biases)

                # 最后加载卷积层的参数
                num_weights = conv.weight.numel()

                # 和上面过程一样
                conv_weights = torch.from_numpy(weights[ptr:ptr + num_weights])
                ptr = ptr + num_weights

                conv_weights = conv_weights.view_as(conv.weight.data)
                conv.weight.data.copy_(conv_weights)


# In[7]:


def get_test_input():
    img = cv2.imread('./dog-cycle-car.png')
    img = cv2.resize(img, (416, 416))
    # (3,416,416)
    img_ = img.transpose((2, 0, 1))
    img_ = img_[np.newaxis, :, :, :] / 255.
    img_ = torch.from_numpy(img_).float()
    img_ = Variable(img_)
    return img_


'''
该张量的形状为1 x 10647 x 85。
第一维是批处理大小，由于我们使用了单个图像，
因此批量大小仅为1。对于批次中的每个图像
我们都有一个10647 x 85的表格。
每个表的行都表示一个边界框。
（4个bbox属性，1个客观分数和80个分类的分数）
'''
# model = Darknet('cfg/yolov3.cfg')
# inp = get_test_input()
# pred = model(inp,torch.cuda.is_available())
# print(pred.shape)


# In[ ]:


# In[9]:


# model = Darknet('cfg/yolov3.cfg')
# model.load_weights('cfg/yolov3.weights')


# In[ ]:


# In[11]:


# def write_results(prediction,confidence,num_classes,nms_conf=0.4):
#     #对于prediction有B*10647个边界框，如果object检测预测值小于confidence
#     #则忽略
#     #在prediction第二维加入一维，代表conf_mask
#     conf_mask = (prediction[:,:,2]>confidence).float().unsqueeze(2)
#     prediction = prediction*conf_mask
#
#
#     box_corner = prediction.new(prediction.shape)
#     box_corner[:, :, 0] = (prediction[:, :, 0] - prediction[:, :, 2] / 2)
#     box_corner[:, :, 1] = (prediction[:, :, 1] - prediction[:, :, 3] / 2)
#     box_corner[:, :, 2] = (prediction[:, :, 0] + prediction[:, :, 2] / 2)
#     box_corner[:, :, 3] = (prediction[:, :, 1] + prediction[:, :, 3] / 2)
#     prediction[:, :, :4] = box_corner[:, :, :4]
#
#     batch_size = prediction.size(0)
#
#     write = False
#
#     for ind in range(batch_size):
#         image_pred = prediction[ind]  # image Tensor
#         # confidence threshholding
#         # 执行非极大值抑制
#         max_conf, max_conf_score = torch.max(image_pred[:, 5:5 + num_classes], 1)
#         max_conf = max_conf.float().unsqueeze(1)
#         max_conf_score = max_conf_score.float().unsqueeze(1)
#         seq = (image_pred[:, :5], max_conf, max_conf_score)
#         image_pred = torch.cat(seq, 1)
# # In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:
