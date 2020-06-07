# tempConvert.py 温度转换方法
tempStr = input("请输入带有符号的温度值:")
if len(tempStr) > 1:
    if tempStr[-1] in ['F', 'f']:
        C = (eval(tempStr[0:-1]) - 32) / 1.8
        print("转换后的温度为：{:.2f}C".format(C))
    elif tempStr[-1] in ['C', 'c']:
        F = eval(tempStr[0:-1]) * 1.8 + 32
        print("转换后的温度为：{:.2f}F".format(F))
    else:
        print("输入格式错误")
else:
    print("输入错误")
