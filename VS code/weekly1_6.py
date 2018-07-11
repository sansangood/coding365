import math
a =int(input())
b =int(input())
c =int(input())
T = b*b-4*a*c 

if T>=0:
    x1 = (-b+math.sqrt(T))/(2.0*a) 
    x2 = (-b-math.sqrt(T))/(2.0*a)
    print('%.1f'%x1)
    print('%.1f'%x2)
elif T<0:
    x11 = -b/(2.0*a)
    x12 = math.sqrt(-T)/(2.0*a)
    print('%.1f+%.1fi'%(x11,x12))
    print('%.1f-%.1fi'%(x11,x12))