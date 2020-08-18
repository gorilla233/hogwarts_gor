class House:
    # 静态属性->变量，类变量，类之中，方法之外
    door = 'red'
    floor = 'white'
    # 动态属性->方法（函数）
    # 构造函数，类实例化的时候直接执行
    def __init__(self):
        # 实例变量，类中，方法之内，以self.方法来定义
        # 作用域为所有方法
        print(self.door)

    def sleep(self):
        # 普通变量，类之中，方法之中，不以self.开头
        shuijiao = "睡觉"
        print(shuijiao)
    def cook(self):
        print('房子可以做饭')

# 实例化->变量=类()
north_house = House()
china_house = House()
House.door = 'white'
print(House.door)
