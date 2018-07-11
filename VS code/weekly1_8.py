a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
#算各個方案的總資費,opq為總資費
#if如果費用小於等於資費算元資費,else(大於)算實際資費,xyz為各方案最後需付金額
o = a*0.08+b*0.139+c*0.135+d*1.128+e*1.483
if o<=183:
    x = 183
else:
    x = o
p = a*0.07+b*0.130+c*0.121+d*1.128+e*1.483
if p<=383:
    y = 383
else:
    y = p 
q = a*0.06+b*0.108+c*0.101+d*1.128+e*1.483
if q <= 983:
    z =983
else:
    z =q 

#以各方案最後須付金額xyz做比較
if x<y<z or x<z<y:
    print('183')
    print(int(x))
elif y<x<z or y<z<x:
    print('383')
    print(int(y))
else:
    print('983')
    print(int(z))
