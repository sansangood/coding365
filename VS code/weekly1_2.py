#引入外援import math模塊
import math
a =int(input())
b =int(input())
c =int(input())
#sqrt(一種方法,平方根),是不能直接方問的,需有math模塊的導入
x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a) 
#'%.1f'字串格式化,將x1 x2以%代入,.1為小數點第幾位(四捨五入),f是定位點(浮點數)
print("%.1f"%x1)
print("%.1f"%x2)