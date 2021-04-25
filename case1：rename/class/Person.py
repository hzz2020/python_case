class Person():
    def eat(self):
        print("能吃")
#         类里面获取实例属性
        print(f'身高是{self.height}')
        print(f'身高是{self.weight}')
    # 默认调用
    def __init__(self):
        # 添加实例属性
        self.weight = 2000
        self.height = 3000

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def __str__(self):
        return '这是demo'

    def __del__(self):
        print(f'对象已经删除')

# # 实例化
# person = Person()
# print(person)
# person.eat()

p2 = Person(22,33)
print(p2)
p2.eat()


# # 添加属性
# person.height = 180
# person.weight = 150
# # 获取属性
# print(f'身高是{person.height}')
# print(f'体重是{person.weight}')

