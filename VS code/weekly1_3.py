num1 =int(input())
num2 =int(input())
Sum =num1+num2
Difference =abs(num1-num2)
Product =num1*num2
#Quotient為商數
cal =num1/num2
#mathfloor也可無條件捨去
Quotient =int(cal*100)/100
print("Sum:%.2f"%(Sum),sep=' ')
print("Difference:%.2f"%Difference,sep=' ')
print("Product:%.2f"%Product,sep=' ') 
print("Quotient:%.2f"%Quotient,sep=' ') 