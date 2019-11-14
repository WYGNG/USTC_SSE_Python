>第一题

```
import math
pi = math.pi
def main():
	print("成绩转换程序")
	while True:
		print("------------------")
		input_val = eval(input("输入成绩:"))
		if input_val < 0 or input_val > 5:
			print("不合法的输入")
			break
		if(input_val==5):
			print('A')
		elif(input_val==4):
			print('B')
		elif(input_val==3):
			print('C')
		elif(input_val==2):
			print('D')
		elif(input_val==1):
			print('E')
		elif(input_val==0):
			print('F')

if __name__ == "__main__":		
	main()
```

![图片](/Users/xq/Desktop/屏幕快照 2.png)



>第二题

```
class Chaos(object):
	def __init__(self):
		# 以下定义的是默认初始值
		self.x1 = 0.25
		self.x2 = 0.26
		self.numIter = 10
		self.filename = 'chaos.txt'

	# 获取用户输入
	def getInput(self):
		x1 = eval(input('输入第一个数:'))
		x2 = eval(input('输入第二个数:'))
		numIter = int(input('输入次数:'))
		return x1, x2, numIter

	# 
	def printout(self):
		x1, x2, numIter = self.getInput()
	
		print('\nindex',end = '')
		print('\t{0:^6}'.format(x1),end = '')
		print('\t\t{0:^6}'.format(x2))		
		print('--------------------------------')

		for i in range(numIter):
			x1 = 3.9 * x1 * (1 - x1)
			x2 = 3.9 * x2 * (1 - x2)
			print('%d\t%.6f\t\t%.6f' % (i+1, x1, x2))


if __name__ == '__main__':
	chaos = Chaos()
	chaos.printout()
```
>程序结果
>
![图片](/Users/xq/Desktop/屏幕快照.png)




