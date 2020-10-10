from __future__ import division
import torch.nn as nn

def parse_config(config):
    '''
    接受一个配置文件
    返回block列表。 每个块是要建立的神经网络中的一个块。 块在列表中表示为字典
    '''
    file = open(config,'r')
    lines = file.read().split('\n')
    #去除空白行
    lines = [x for x in lines if len(x)>0]
    #去除注释
    lines = [x for x in lines if x[0]!='#']
    #去除左右空格
    lines = [x.rstrip().lstrip() for x in lines]    
    #记录每一个块
    block = {}
    blocks = []
    
    #解析lines列表转化为神经网络的blocks块
    for line in lines:
        #标志一个新的块
        if line[0] == '[':
            #如果这个块不为空
            if (len(block)!=0):
                blocks.append(block)
                block = {}
            block["type"] = line[1:-1].rstrip()     
        else:
            key,value = line.split('=')
            block[key.rstrip()] = value.lstrip()
    blocks.append(block)
    return blocks   
    



#定义空层
class EmptyLayer(nn.Module):
    def __init__(self):
        super(EmptyLayer, self).__init__()
        
class DetectionLayer(nn.Module):
    def __init__(self, anchors):
        super(DetectionLayer, self).__init__()
        self.anchors = anchors

#创建模块。此时blocks是包含所有层的字典
def create_modules(blocks):
    net_info = blocks[0]
    module_list = nn.ModuleList()
    prev_filters = 3
    #记录经过卷积层，当前的通道数量
    output_filters = []
    
    for index,x in enumerate(blocks[1:]):
        module = nn.Sequential()
        #检查block类型
        #为这个block分配新的module
        #添加到module_list
        
        #如果是卷积层
        if(x['type'] == 'convolutional'):
            #获取该层的信息
            activation = x['activation']
            try:
                batch_normalize = int(x['batch_normalize'])
                bias = False
            except:
                batch_normalize = 0
                bias = True
            
            filters = (int)(x['filters'])
            padding = (int)(x['pad'])
            kernel_size = (int)(x['size'])
            stride = (int)(x['stride'])
            
            #如果有填充,保持卷积前后shape保持SAME
            if padding:
                pad = (kernel_size-1)//2
            else:
                pad = 0
            
            #添加卷积层
            conv = nn.Conv2d(prev_filters,filters,kernel_size,stride,pad,bias = bias)
            module.add_module('conv_{0}'.format(index),conv)
            
            #添加批归一化层
            if batch_normalize:
                bn = nn.BatchNorm2d(filters)
                module.add_module('batch_norm_{0}'.format(index),bn)
            
            #查看激活函数
            if activation == 'leaky':
                activn = nn.LeakyReLU(0.1,inplace=True)
                module.add_module('leaky_{0}'.format(index),activn)
                
        #如果是上采样层
        #使用 Bilinear2dUpsampling
        elif (x['type']=='upsample'):
            stride = int(x['stride'])
            upsample = nn.Upsample(scale_factor=2,mode='nearest')
            module.add_module("upsample_{}".format(index), upsample)

        
        #如果是路由层,这边不太明白
        elif (x['type']=='route'):
            x['layers'] = x['layers'].split(',')
            #开始的索引
            start = int(x['layers'][0])
            #尝试有没有结束索引
            try:
                end = int(x['layers'][1])
            except:
                end = 0
                
            if start>0:
                start = start - index
            if end>0:
                end = end - index
            
            #不是很明白，应该是连接操作啊，torch.cat()
            #空层就是为了连接用的。初始化为空层，底下再进行操作。
            route = EmptyLayer()
            #添加路由层
            module.add_module("route_{0}".format(index), route)
            if end < 0 :
                filters = output_filters[index+start]+output_filters[index+end]
            else:
                filters = output_filters[index+start]
            
        #如果是shortcut层。残差网络
        # 空层就是为了连接用的。初始化为空层，底下再进行操作。
        elif (x['type']=='shortcut'):
            shortcut = EmptyLayer()
            module.add_module('shortcut_{0}'.format(index),shortcut)
        
        #如果是yolo层
        elif (x['type'] == 'yolo'):
            mask = x['mask'].split(',')
            mask = [int(x) for x in mask]
            anchors = x['anchors'].split(',')
            anchors = [int(x) for x in anchors]
            anchors = [(anchors[i],anchors[i+1]) for i in range(0,len(anchors),2)]
            #指定的3个anchors
            anchors = [anchors[i] for i in mask]
            
            detection = DetectionLayer(anchors)
            
            module.add_module('Detecion_{}'.format(index),detection)
    
        module_list.append(module)
        #纪录前一个的通道数
        prev_filters = filters
        output_filters.append(filters)
        
    return (net_info,module_list)
            


