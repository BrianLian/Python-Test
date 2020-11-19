import random as r

ran_start = int(input("請輸入亂數起始值:"))
ran_end = int(input("請輸入亂數終始值:"))
inp = int(input("請輸入亂數次數:"))
for i in range(0, inp):
    print("random:{}".format(r.randint(ran_start, ran_end)))
