from python.homework_python.TongLao.TongLao import TongLao


class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")

game = XuZhu(1000,200)
game.read()