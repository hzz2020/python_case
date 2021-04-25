# 多态
class Dog(object):
    # 定义类属性
    tooth = 4
    # 私有类属性
    __tooth = 8

    def __init__(self):
        self.count = 22

    def add(self, m):
        print(f'self is {self} @Dog.add')
        self.count += m

    def work(self):
        print(f'指哪打哪')

    # 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    # 定义静态方法
    @staticmethod
    def print_info():
        print(f'这是一个静态方法')


class ArmyDog(Dog):
    def work(self):
        print(f'追击敌人')

    def __init__(self):
        self.count = 10

    def add(self, m):
        print(f'self is {self} @ArmyDog.add')
        # super()的用法
        super().add(m)
        self.count += m
        
class DrugDog(Dog):
    def work(self):
        print(f'追查毒品')

class Person(object):
    def work_with_dog(self, dog):
        dog.work()

dg = Dog()
ad = ArmyDog()
dd = DrugDog()
# 通过类名访问类属性
print(f'tooth1 = {Dog.tooth}')
# 通过对象访问类属性
print(f'tooth2 = {ad.tooth}')
print(f'tooth3 = {dd.tooth}')
# 修改类属性是不能通过实例对象去修改的，只能通过类对象
Dog.tooth = 10
print(f'tooth1 = {Dog.tooth}')
print(f'tooth2 = {ad.tooth}')
print(f'tooth3 = {dd.tooth}')
ad.tooth = 20
dd.tooth = 40
print(f'tooth1 = {Dog.tooth}')
print(f'tooth2 = {ad.tooth}')
print(f'tooth3 = {dd.tooth}')

result = dg.get_tooth()
print(result)
# 类名和实例对象都可以调用静态方法
Dog.print_info()
dg.print_info()

person = Person()
person.work_with_dog(dg)
person.work_with_dog(ad)
person.work_with_dog(dd)


ad.add(300)
print(dg.count)
print(ad.count)