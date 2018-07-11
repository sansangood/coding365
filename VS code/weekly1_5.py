#分割
x = input()
x = x.split(' ')
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
e = int(x[4])
#數學公式展開以轉換成程式碼
ave = (a+b+c+d+e)/5
#^是x的y次方
var = ((a-ave)**2+(b-ave)**2+(c-ave)**2+(d-ave)**2+(e-ave)**2)/5
ad =var**(0.5)  
#小數點第二位無條件捨去,需先乘100,取出整數int,再除100
#輸出時能需使用"%.02f"%
x1 = int(ave*100)/100
x2 = int(var*100)/100
x3 = int(ad*100)/100
print('%.2f'%x1)
print('%.2f'%x2)
print('%.2f'%x3)