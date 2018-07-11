import random
secrect =random.randint(1,10)
print('----我愛C魚工作室----')
a =input('不妨猜一下小魚心裡想的數字:')
guess =int(a)
while guess !=secrect:
    a =input('哎呀!猜錯了,在猜一次吧:')
    guess =int(a)
    if guess ==secrect:
        print("哇草,你是小甲魚心裡的蛔蟲嗎?")
        print("哼,猜中了也沒有獎勵")
    else:
        if guess>secrect:
            print("哥,大了大了")
        else:
            print("嘿,小了小了")
print("遊戲結束,不玩了")