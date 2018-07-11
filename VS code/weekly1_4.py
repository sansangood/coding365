x =input()
#輸入為字串'4 1 1'(假設),故需要先spilt(' ')分割,以空格分割,會得到['4','1','1'](假設)的串列
x =x.split(' ')
#將數字分別切割出來,並轉為整數
a =int(x[0])
b =int(x[1])
c =int(x[2])
#設定if條件,elif是else if的綜合,運算速度較都是if快
if  a+b<=c or a+c<=b or c+b<=a or a<0 or b<0 or c<0:
    print(1)
elif  a==b==c:
    print(2)
elif  a==b!=c or a==c!=b or b==c!=a:
    print(3)
else:
    print(4)

