class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        name = str(input("who are you?"))
        if name == 'WYZ':
            print("师弟！！！！")
        elif name == 'LQS':
            print("呸，贱人")
        elif name == 'DCQ':
            print("叛徒！我杀了你")
        else:
            print("please input a true name")

    def fight_zms(self, e_hp, e_power):
        self.power = self.power * 10
        self.hp = self.hp / 2
        while True:
            self.hp = self.hp - e_power
            e_hp = e_hp - self.power
            print(self.hp)
            if self.hp <= 0:
                print("You win")
                break
            elif e_hp <= 0:
                print("I win")
                break

# game = TongLao(1000,200)
# game.fight_zms(1000,200)



