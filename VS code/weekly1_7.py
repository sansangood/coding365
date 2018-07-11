x =int(input())
y =int(input())
z =int(input())

#變數的初始化
Total=0

#Total+像是個儲存槽一樣，可將各階段的結果賦值總加在一起
if 1<=x<=10:
    Total+=x*380
elif 11<=x<=20:
	Total+=x*380*0.9
elif 21<=x<=30:
	Total+=x*380*0.85
else :
	Total+=x*380*0.8

if 1<=y<=10:
	Total+=y*1200
elif 11<=y<=20:
	Total+=y*1200*0.95
elif 21<=y<=30:
	Total+=y*1200*0.85
else  :
	Total+=y*1200*0.8

if 1<=z<=10:
	Total+=z*180
elif 11<=z<=20:
	Total+=z*180*0.85
elif 21<=z<=30:
	Total+=z*180*0.8
else  :
	Total+=z*180*0.7
#將Total取整數,如不這麼做python會自動默認到小數點第一位
Total =int(Total)
print(Total)