print ('''steam汇率计算''')
while (1):
    a = input ("请输入steam价格")
    b = input ("请输入buff价格")
    if  a ==("") or b ==(""):
        break
    else:
        c = 100/115*float(a) 
        d = float(b) / c
        print ("steam价格为"+str(a))
        print ("buff价格为"+str(b))
        print (("steam除去手续费得到")+(str(format(c, ".2f"))))
        print (("buff转换steam所汇率为")+(str(format(d * 100, ".2f")+"%")))

