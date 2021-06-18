

#水仙花数

def daffodil_number():
    """
    100,1000的水仙花数
    """
    shuixianhuashu_list = []

    for i in range(100, 1000):
        a = i // 100
        b = (i - a * 100) // 10
        c = (i - a * 100 - b * 10)

        if i==(pow(a,3)+pow(b,3)+pow(c,3)):
            shuixianhuashu_list.append(i)
    print(f"100-1000之间的水仙花数有{len(shuixianhuashu_list)}个,具体都有：{shuixianhuashu_list}")



def daffodil_number2(number):
    """
    number int && length=3
    """
    str_number = str(number)
    if len(str_number)==3:
        a,b,c = int(str_number[0]),int(str_number[1]),int(str_number[2])
        if a**3+b**3+c**3 == number:
            print(True,"是水仙花数")
        else:
            print(False,"不是水仙花数")
    else:
        print(f"当前输入的不是三位数")

# daffodil_number2(153)
