import math
import random

print(math.sqrt(9))
print(random.random())



from random import randint

print(randint(1,10))

from math import *

print(math.sqrt(16))

# as 别名
import time as tt
tt.sleep(1)
print('hello python')

from time import sleep as sl
sl(1)
print('hello hhhh')



from my_module1 import *

testA(10, 20)
# testB 没有在all列表中
# testB(20, 4)

from mypackage import *
my_module1.info_print1()
# my_module2没有在all列表中
# my_module2.info_print2()

