class Jiaju():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具{self.name},占地面积{self.area}'


class Home():
    def __init__(self, address, area):
        self.address = address

        self.area = area

        self.area_free = area

        self.jiajus = []

    def __str__(self):
        return f'家位置在{self.address},占地面积{self.area},空闲面积{self.area_free},家具有{self.jiajus}'

    def add_jiaju(self, item):
        if item.area <= self.area_free:
            self.jiajus.append(item.name)
            self.area_free -= item.area
        else:
            print('面积不够，放不进去此家具')

bed = Jiaju('床',6)
sofa = Jiaju('沙发', 10)

home = Home('湖南长沙', 40)
print(home)

home.add_jiaju(bed)
print(home)
home.add_jiaju(sofa)
print(home)
