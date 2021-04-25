# 继承的特点
# 1、子类默认拥有父类的所有属性和方法
# 2、子类重写父类的属性和方法
# 3、子类调用父类的属性和方法


# Father继承自object
class Father(object):
    def __init__(self):
        self.age = 60
        self.__money = 20000
    def print_info(self):
        print(f'年龄 = {self.age}, 金额有{self.__money}')

    def __print_money(self):
        print(f'哈哈哈哈哈')

# Son继承自Father
class Son(Father):
    def __init__(self):
        self.age = 35

    def print_info(self):
        print(f'年龄 = {self.age}, 金额访问不了')
        super().__init__()
        super().print_info()

son = Son();
son.print_info()


class Animal(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


    def __init__(self):
        self.gongfu = '乾坤大挪移'
    def make_run(self):
        print(f'运用{self.gongfu}打架')

class Person(Animal):
    def __init__(self):
        self.gongfu = '降龙十八掌'
    def make_run(self):
        print(f'运用{self.gongfu}打架')

class Teacher(Person):
    def __init__(self):
        self.gongfu = '黯然销魂掌'
    def make_run(self):
        # 如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用子类初始化
        self.__init__()
        print(f'自创了{self.gongfu}打架')

    # 调用父类方法，但是为了保证调用到的也是父类的属性，必须在调用方法之前调用父类的初始化
    def make_master_run(self):
        Person.__init__(self)
        Person.make_run(self)

    def make_school_run(self):
        Animal.__init__(self)
        Animal.make_run(self)

stu = Teacher()
# **** 多继承，调用第一个继承类的同名属性和方法 ****
print(stu.gongfu)
stu.make_run()
# **** 子类调用父类同名方法 ****
stu.make_master_run()
stu.make_school_run()

print(Teacher.__mro__)
