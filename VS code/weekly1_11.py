ax1 = int(input())
ax2 = int(input())
bx1 = int(input())
bx2 = int(input())
cx1 = int(input())
cx2 = int(input())
list1 =(ax1,ax2,bx1,bx2,cx1,cx2)
list1 =[int(i) for i in list1]
print(max(list1)-min(list1))