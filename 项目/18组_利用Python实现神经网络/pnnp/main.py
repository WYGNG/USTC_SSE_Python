import NeuralNetwork as nn
import numpy as np
import dill as pickle
import matplotlib.pyplot as plt

#使用csvFile文件中的数据训练神经网络neuralNetwork
def train(neuralNetwork,csvTrainFile):
    print("训练开始！！！")
    for i in range(10):
        trainFileObject=open(csvTrainFile,"r")
        line=trainFileObject.readline()
        while line!="":
            list=line.split(",")
            number=int(list[0])
            inputDataTemp=np.array(list[1:],dtype="float")
            inputData=(inputDataTemp/255.0)*0.99+0.01
            targetData=np.array([0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,])
            targetData[number]=0.99
            neuralNetwork.train(inputData,targetData) 
            line=trainFileObject.readline()
        trainFileObject.close()
    print("训练完毕！！！")

def test(neuralNetwork,csvTestFile):
    print("测试开始！！！")
    arr1=np.zeros(10,dtype="int")
    arr2=np.zeros(10,dtype="int")
    testFileObject=open(csvTestFile,"r")
    line=testFileObject.readline()
    while line!="":
        list=line.split(",")
        number=int(list[0])
        arr1[number]+=1
        inputDataTemp=np.array(list[1:],dtype="float")
        inputData=(inputDataTemp/255.0)*0.99+0.01
        outputData=neuralNetwork.query(inputData)
        index=np.argmax(outputData)

        if number==index:
            arr2[number]+=1
        line=testFileObject.readline()
    testFileObject.close()
    print("正确个数：",np.sum(arr2)," 错误个数：",np.sum(arr1)-np.sum(arr2))
    print("测试结束！！！")
    arr=arr2/arr1
    plt.bar(range(10),arr)
    plt.xlabel("number")
    plt.ylabel("accuracy")
    plt.ylim((0.80,1.00))

#将mnist数据集合转换为csv文件格式
def convert(imageFile,labelFile,outputFile,dataCount):
    imageFileObject=open(imageFile,"rb")
    labelFileObject=open(labelFile,"rb")
    outputFileObject=open(outputFile,"w")
    
    imageFileObject.read(16)
    labelFileObject.read(8)
    images=[]
    
    for i in range(dataCount):
        image=[ord(labelFileObject.read(1))]
        for j in range(784):
            image.append(ord(imageFileObject.read(1)))
        images.append(image)
    
    for image in images:
        outputFileObject.write(",".join(str(pix) for pix in image)+"\n")
    
    imageFileObject.close()
    labelFileObject.close()
    outputFileObject.close()

def convertFile():
    convert("mnist_data/train-images.idx3-ubyte","mnist_data/train-labels.idx1-ubyte","data/train_60000.csv",60000)
    convert("mnist_data/t10k-images.idx3-ubyte","mnist_data/t10k-labels.idx1-ubyte","data/test_10000.csv",10000)

def testSmall(neuralNetwork):
    correctCount=0
    errorCount=0
    fig=plt.figure()
    plt.subplots_adjust(wspace=1,hspace=1)
    subplot=1
    testFileObject=open("small_mnist_data/mnist_test_10.csv","r")
    line=testFileObject.readline()
    while line!="":
        list=line.split(",")
        number=int(list[0])
        inputDataTemp=np.array(list[1:],dtype="float")
        inputData=(inputDataTemp/255.0)*0.99+0.01
        outputData=neuralNetwork.query(inputData)
        index=np.argmax(outputData)
        if(index==number):
            correctCount+=1
        else:
            errorCount+=1

        ax=fig.add_subplot(4,3,subplot)
        ax.imshow(inputData.reshape(28,28))
        subplot+=1
        ax.set(title="real: "+str(number)+" test: "+str(index))

        line=testFileObject.readline()
    fig.suptitle("correct:"+str(correctCount)+" error:"+str(errorCount))
    testFileObject.close()