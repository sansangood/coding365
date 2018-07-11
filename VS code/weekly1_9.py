x =input()
x =x.split(' ')
a =int(x[0])
b =int(x[1])
c =int(x[2])
#判斷是否無三角形
if a+b<=c or a+c<=b or c+b<=a or a<=0 or b<=0 or c<=0:
    print('Not Triangle')
#判斷是否為直角三角形(兩邊的平方和等於第三邊的平方)
elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
    print('Right Triangle')
    #判斷是否為鈍角三角形(兩邊的平方和小於第三邊的平方)
elif a*a+b*b<c*c or a*a+c*c<b*b or b*b+c*c<a*a:
    print('Obtuse Triangle')
    #判斷是否為銳角三角形(兩邊的平方和大於第三邊的平方)
else :
    print('Acute Triangle') 