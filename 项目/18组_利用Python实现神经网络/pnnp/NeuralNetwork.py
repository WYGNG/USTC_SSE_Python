#使用到numpy模块
import numpy as np
import scipy.special
import dill as pickle

#四层神经网络模型
class FNN:
    #搭建神经网络模型
    def __init__(self,inputNodes,outputNodes,firstNodes=128,secondNodes=128,k=np.e/10.0):
        #输入层结点个数
        #int
        self.inputNodes=inputNodes
        #第一个隐藏层结点个数
        #int: 默认为128
        self.firstNodes=firstNodes
        #第二个隐藏层结点个数
        #int: 默认为128
        self.secondNodes=secondNodes
        #输出层结点个数
        #int
        self.outputNodes=outputNodes
        #输入层与第一个隐藏层之间的权值矩阵
        #np.array: self.firstNodes*self.inputNodes
        #均值为0，方差为(self.firstNodes)^(-0.5)的随机元素值
        wifRow=self.firstNodes              #矩阵WIF行数
        wifCol=self.inputNodes              #矩阵WIF列数
        wifLoc=0                            #矩阵WIF元素均值
        wifScale=pow(self.firstNodes,-0.5)  #矩阵WIF元素方差
        self.WIF=np.random.normal(wifLoc,wifScale,(wifRow,wifCol))
        #第一个隐藏层与第二个隐藏层之间的权值矩阵
        #np.array: self.secondNodes*self.firstNodes
        #均值为0，方差为(self.secondNodes)^(-0.5)的随机元素值
        wfsRow=self.secondNodes             #矩阵WFS行数
        wfsCol=self.firstNodes              #矩阵WFS列数
        wfsLoc=0                            #矩阵WFS元素均值
        wfsScale=pow(self.secondNodes,-0.5)  #矩阵WFS元素方差
        self.WFS=np.random.normal(wfsLoc,wfsScale,(wfsRow,wfsCol))
        #第二个隐藏层与输出层之间的权值矩阵
        #np.array: self.outputNodes*self.secondNodes
        #均值为0，方差为(self.outputNodes)^(-0.5)的随机元素值
        wsoRow=self.outputNodes
        wsoCol=self.secondNodes
        wsoLoc=0
        wsoScale=pow(outputNodes,-0.5)
        self.WSO=np.random.normal(wsoLoc,wsoScale,(wsoRow,wsoCol))
        #神经网络的抑制函数func
        #默认为scipy.special.expit(x)
        #其为1/(1+e^(-x))
        self.func=lambda x: scipy.special.expit(x)
        #学习率k
        #int: 默认为e/10.0
        self.k=k

    #输入数据经由四层神经网络获得输出数据
    def query(self,InputData):
        #输入数据为InputData
        #np.array: self.inputNodes

        #获取第一个隐藏层的组合输入数组FL
        #InputDataTemp
        #np.array: self.inputNodes*1
        InputDataTemp=InputData.reshape(self.inputNodes,1)
        #FLTemp
        #np.array: self.firstNodes*1
        FLTemp=np.dot(self.WIF,InputDataTemp)
        #FL
        #np.array: self.firstNodes
        FL=FLTemp.reshape(self.firstNodes)

        #对FL应用抑制函数获取第一个隐藏层的输出数组FR
        #np.array: self.firstNodes
        FR=self.func(FL)

        #获取第二个隐藏层的组合输入数组SL
        #FRTemp
        #np.array: self.firstNodes*1
        FRTemp=FR.reshape(self.firstNodes,1)
        #SLTemp
        #np.array: self.secondNodes*1
        SLTemp=np.dot(self.WFS,FRTemp)
        #SL
        #np.array: self.secondNodes
        SL=SLTemp.reshape(self.secondNodes)

        #对SL应用抑制函数获取第二个隐藏层的输出数组SR
        #np.array: self.secondNodes
        SR=self.func(SL)

        #获取输出层的组合输入数组OL
        #SRTemp
        #np.array: self.secondNodes*1
        SRTemp=SR.reshape(self.secondNodes*1)
        #OLTemp
        #np.array: self.outputNodes*1
        OLTemp=np.dot(self.WSO,SRTemp)
        #OL
        #np.array: self.outputNodes
        OL=OLTemp.reshape(self.outputNodes)

        #对OL应用输出函数获取输出层的输出数组OR
        OR=self.func(OL)

        #返回输出数据OR
        return OR

    #训练神经网络模型
    def train(self,InputData,TargetData):
        #目标数据为TargetData
        #np.array: self.outputNodes
        #输入数据为InputData
        #np.array: self.inputNodes
        #获取第一个隐藏层的组合输入数组FL
        #InputDataTemp
        #np.array: self.inputNodes*1
        InputDataTemp=InputData.reshape(self.inputNodes,1)
        #FLTemp
        #np.array: self.firstNodes*1
        FLTemp=np.dot(self.WIF,InputDataTemp)
        #FL
        #np.array: self.firstNodes
        FL=FLTemp.reshape(self.firstNodes)
        #对FL应用抑制函数获取第一个隐藏层的输出数组FR
        #np.array: self.firstNodes
        FR=self.func(FL)
        #获取第二个隐藏层的组合输入数组SL
        #FRTemp
        #np.array: self.firstNodes*1
        FRTemp=FR.reshape(self.firstNodes,1)
        #SLTemp
        #np.array: self.secondNodes*1
        SLTemp=np.dot(self.WFS,FRTemp)
        #SL
        #np.array: self.secondNodes
        SL=SLTemp.reshape(self.secondNodes)
        #对SL应用抑制函数获取第二个隐藏层的输出数组SR
        #np.array: self.secondNodes
        SR=self.func(SL)
        #获取输出层的组合输入数组OL
        #SRTemp
        #np.array: self.secondNodes*1
        SRTemp=SR.reshape(self.secondNodes*1)
        #OLTemp
        #np.array: self.outputNodes*1
        OLTemp=np.dot(self.WSO,SRTemp)
        #OL
        #np.array: self.outputNodes
        OL=OLTemp.reshape(self.outputNodes)
        #对OL应用输出函数获取输出层的输出数组OR
        #OR
        #np.array: self.outputNodes
        OR=self.func(OL)

        #调整WSO矩阵
        #获取输出层的误差数组OE
        #np.array: self.outputNodes
        OE=TargetData-OR
        #获取WSO矩阵对应的梯度矩阵gradsWSO
        #np.array: self.outputNodes*self.secondNodes
        #获取gradWSO的左乘矩阵gradWSODotLeft
        #gradsWSODotLeftTemp
        #np.array: self.outputNodes
        gradsWSODotLeftTemp=self.k*OE*OR*(1-OR)
        #gradWSODotLeft
        #np.array: self.outputNodes*1
        gradsWSODotLeft=gradsWSODotLeftTemp.reshape(self.outputNodes,1)
        #获取gradWSO的右乘矩阵gradWSODotRight
        #np.array: 1*secondNodes
        gradsWSODotRight=SR.reshape(1,self.secondNodes)
        #gradsWSO
        #np.array: self.outputNodes*self.secondNodes
        gradsWSO=np.dot(gradsWSODotLeft,gradsWSODotRight)
        #根据gradWSO调整WSO矩阵
        self.WSO+=gradsWSO

        #调整WFS矩阵
        #根据OE获取第二个隐藏层的误差数组SE
        #np.array: self.secondNodes
        #WSOTemp
        #np.array: self.secondNodes*self.outputNodes
        WSOTemp=self.WSO.T
        #OETemp
        #np.array: self.outputNodes*1
        OETemp=OE.reshape(self.outputNodes,1)
        #SETemp
        #np.array: self.secondNodes*1
        SETemp=np.dot(WSOTemp,OETemp)
        #SE
        #np.array: self.secondNodes
        SE=SETemp.reshape(self.secondNodes)
        #获取WFS矩阵对应的梯度矩阵gradsWFS
        #np.array: self.secondNodes*self.firstNodes
        #获取gradWFS的左乘矩阵gradWFSDotLeft
        #gradsWFSDotLeftTemp
        #np.array: self.secondNodes
        gradsWFSDotLeftTemp=self.k*SE*SR*(1-SR)
        #gradWFSDotLeft
        #np.array: self.secondNodes*1
        gradsWFSDotLeft=gradsWFSDotLeftTemp.reshape(self.secondNodes,1)
        #获取gradWFS的右乘矩阵gradWFSDotRight
        #np.array: 1*self.firstNodes
        gradsWFSDotRight=FR.reshape(1,self.firstNodes)
        #gradsWFS
        #np.array: self.secondNodes*self.firstNodes
        gradsWFS=np.dot(gradsWFSDotLeft,gradsWFSDotRight)
        #根据gradWSO调整WSO矩阵
        self.WFS+=gradsWFS

        #调整WIF矩阵
        #根据SE获取第一个隐藏层的误差数组SE
        #np.array: self.firstNodes
        #WFSTemp
        #np.array: self.firstNodes*self.secondNodes
        WFSTemp=self.WFS.T
        #SETemp
        #np.array: self.secondNodes*1
        SETemp=SE.reshape(self.secondNodes,1)
        #FETemp
        #np.array: self.firstNodes*1
        FETemp=np.dot(WFSTemp,SETemp)
        #FE
        #np.array: self.firstNodes
        FE=FETemp.reshape(self.firstNodes)
        #获取WIF矩阵对应的梯度矩阵gradsWIF
        #np.array: self.firstNodes*self.inputNodes
        #获取gradWFS的左乘矩阵gradWIFDotLeft
        #gradsWIFDotLeftTemp
        #np.array: self.firstNodes
        gradsWIFDotLeftTemp=self.k*FE*FR*(1-FR)
        #gradWIFDotLeft
        #np.array: self.firstNodes*1
        gradsWIFDotLeft=gradsWIFDotLeftTemp.reshape(self.firstNodes,1)
        #获取gradWIF的右乘矩阵gradWIFDotRight
        #np.array: 1*self.inputNodes
        gradsWIFDotRight=InputData.reshape(1,self.inputNodes)
        #gradsWIF
        #np.array: self.firstNodes*self.inputNodes
        gradsWIF=np.dot(gradsWIFDotLeft,gradsWIFDotRight)
        #根据gradWIF调整WIF矩阵
        self.WIF+=gradsWIF

#将神经网络模型neuralNetwork保存至文件file
def write(neuralNetwork,file):
    #使用pickle模块将当前对象self写入file
    fileObject=open(file,"wb")
    o=pickle.dumps(neuralNetwork)
    fileObject.write(o)
    fileObject.close()

#从文件file中读取的神经网络模型
def copy(file):
    fileObject=open(file,"rb")
    return pickle.load(fileObject)
