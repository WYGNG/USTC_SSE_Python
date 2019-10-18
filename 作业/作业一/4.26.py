variable = eval(input("Enter a three-digit integer:"))  #输入一个3位整数
a = variable//100   #a为百位数
b = variable%10     #b为个位数
if a == 0 or a > 9: #检查输入的数是否为三位数
    print(variable,"is not a three-digit integer")
elif a == b:        #个位数和百位数相等则为回文数
    print(variable,"is a palindrome") 
else:
    print(variable,"is not a palindrome")

