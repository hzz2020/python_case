import os
import re
import sys

# 添加文本
def add_mark(path): 
    # 选择操作，并对操作进行处理
    option = input("请选择功能数值:\n1：名称之前添加\n2：名称之后添加\n其他数字：返回\n")
    while True:
        try:
            option = float(option)
            break
        except:
            option = input("输入错误!!!\n请选择功能数值:\n1：名称之前添加\n2：名称之后添加\n其他数字：返回\n")
    option = int(option)
    if option != 1 and option != 2 :
        main()
    # 对要添加的内容进行校验
    add_str = input("请输入需要添加的内容:")
    while True:
        if not add_str.strip():
            add_str = input("要添加的内容不能为空！！！\n请输入需要添加的内容:")
        else:
            break
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(path)
    # 当前工作目录文件列表
    fileList = os.listdir(path)
    # 循环来匹配要处理的文件名
    for fileName in fileList:
        # 不等于本程序文件，则进行修改，防止修改本程序文件（ps:程序运行中不能自己把自己的名字改了！！！）
        if fileName != os.path.split(__file__)[-1]:          
            # 分离文件名字和后缀名，防止修改文件后缀   
            nameList = os.path.splitext(fileName)
            afterName = ""
            if option == 1:
                # 前缀
                afterName = add_str + nameList[0]
            else:
                # 后缀
                afterName = nameList[0] + add_str
            # 改名
            os.rename(fileName, afterName+nameList[1])
            # os.rename(os.path.join(path, fileName), os.path.join(path, afterName+nameList[1]))

# 替换(删除)文本
def replace_mark(path):
    # 对查找内容进行校验，要替换的内容为空表示删除操作
    old_str = input("请输入要查找的内容:")
    while True:
        if not old_str.strip():
            old_str = input("要查找的内容不能为空！！！\n请输入需要查找的内容:")
        else:
            break
    last_str = input("请输入要替换成的内容:")
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(path)
    # 当前工作目录文件列表
    fileList = os.listdir(path)
    # 循环来匹配要处理的文件名
    for fileName in fileList:
        # 目录和文件判断
        if os.path.isdir(os.path.join(path, fileName)):
            # 匹配文件名中是否有要查找的内容
            if old_str in fileName:
                afterName = fileName.replace(old_str, last_str)
                # 如果替换后文件名字为空，则不处理；
                if not afterName.strip():
                    print(fileName + "替换后名字为空，系统不允许！")
                    continue
                else:
                    os.rename(fileName, afterName)
        elif os.path.isfile(os.path.join(path, fileName)):
            # 不等于本程序文件，则进行修改，防止修改本程序文件（ps:程序运行中不能自己把自己的名字改了！！！）
            if fileName != os.path.split(__file__)[-1]:          
                # 分离文件名字和后缀名，防止修改文件后缀   
                nameList = os.path.splitext(fileName)
                # 匹配文件名中是否有要查找的内容
                if old_str in nameList[0]:
                    # 利用replace函数操作
                    afterName = nameList[0].replace(old_str, last_str)
                    # 如果替换后文件名字为空，则不处理；
                    if not afterName.strip():
                        print(fileName + "替换后名字为空，系统不允许！")
                        continue
                    else:
                        os.rename(fileName, afterName+nameList[1])
                        # os.rename(os.path.join(path, fileName), os.path.join(path, afterName+nameList[1]))
    print("操作完成\n")

# 主函数
def main():
    # 确认需要编辑的工作目录
    currentpath = input("请输入工作目录(全路径):")
    while True:
        if not currentpath.strip(): # 目录为空，则获取当前所在目录
            currentpath = os.getcwd()
            break
        else: # 目录不为空，则要判断输入的是不是一个合法的目录
            if not os.path.isdir(currentpath):
                input("目录不存在！！！请输入工作目录(全路径):")
            else:
                break
    print("工作目录:" + currentpath)
    # 选择操作 并对用户输入进行校验
    option = input("请选择功能数值:\n1：添加文本\n2：替换文本\n3：格式处理\n其他数字：退出程序\n")
    while True:
        try:
            option = float(option)
            break
        except:
            option = input("输入错误!!!\n请选择功能数值:\n1：添加文本\n2：替换文本\n3：格式处理\n其他数字：退出程序\n")
    option = int(option)
    # 
    if option == 1:
        add_mark(currentpath)
    elif option == 2:
        # remove_mark()
        replace_mark(currentpath)
    elif option == 3:
        print("还未开发...敬请期待")
        exit()
    else:
        exit()

# 运行
if __name__ == "__main__":
    main()
