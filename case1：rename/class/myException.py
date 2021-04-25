
# 异常语法
try:
    print(f'可能发生异常的代码')
except:
    print(f'如果出现异常执行的代码')
else:
    print(f'没有异常执行的代码')
finally:
    print(f'无论是否异常都会执行的代码')

# 捕获异常描述信息
try:
    print(1/0)  # print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)

# 捕获所有异常 【Exception是程序异常类的父类】
try:
    print(num)
except Exception as result:
    print(result)
else:
    print(f'没有出现异常')

import time

try:
    f = open('text.txt', 'r')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()

            # 读取完成要退出循环
            if len(con) == 0:
                break

            # time.sleep(3)
            print(con)
    except:
        print('程序被意外终止')
except Exception as result:
    print('该文件不存在')
else:
    print('没异常')
finally:
    f.close()


# 自定义异常
# 1自定义异常类
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的密码长度为{self.length}, 不能少于{self.min_len}'


def main():
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            raise ShortInputError(len(con), 3)
    except Exception as  result:
        print(result)
    else:
        print('密码已经输入完成')

main()