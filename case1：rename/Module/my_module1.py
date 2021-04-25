__all__ = ['testA']

def testA(a,b):
    print(a+b)


def testB(a, b):
    print(a*b)

# 只有当前文件夹中调用该函数，其他导入的文件内不符合该条件，则不执行testA函数调用
if __name__ == '__main__':
    testA(1,4)
    testB(2,4)