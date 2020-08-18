class Game():
    def __init__(self,my_hp, your_hp):
        self.my_hp = my_hp
        self.my_power = 200
        self.your_hp = your_hp
        self.your_power = 199
    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.your_power
            self.your_hp = self.your_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <=0:
                print("I am failed")
                break
            elif self.your_hp <=0:
                print("I win")
                break
#
# game = Game()
# game.fight()

class HouYi(Game):
    # 如果重名的话，子类的属性会覆盖掉父类的属性
    def __init__(self):
        self.defense = 100
        # 继承父类的构造方法，如果父类有形参，需要传递参数
        super().__init__(1000, 1300)


    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <=0:
                print("I am failed")
                break
            elif self.your_hp <=0:
                print("I win")
                break
game = HouYi()
game.fight()