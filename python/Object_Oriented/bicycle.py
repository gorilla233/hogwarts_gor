class Bicycle:
    def run(self, km):
        print(f"一共用自行车骑了{km}公里")

# bike = Bicycle()
# bike.run(1)
# 非继承
# class EBicycle:
#     def __init__(self, valume):
#         self.valume = valume
#
#     def fill_charge(self, vol):
#         self.valume = vol + self.valume
#         print(f"充了{vol}度电，现在{self.valume}度电")
#
#     def run(self, km):
#         power_km = self.valume * 10
#         if power_km > km:
#             print(f"我使用电瓶电量骑了{km}公里")
#         else:
#             print(f"我使用电瓶骑了{power_km}公里")
#             bike = Bicycle()
#             bike.run(km - power_km)
#
# ebike = EBicycle(10)
# ebike.run(200)

# ebike = EBicycle(10)
# ebike.fill_charge(3)
# 继承
class EBicycle(Bicycle):
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, vol):
        self.valume = vol + self.valume
        print(f"充了{vol}度电，现在{self.valume}度电")

    def run(self, km):
        power_km = self.valume * 10
        if power_km > km:
            print(f"我使用电动车电量骑了{km}公里")
        else:
            print(f"我使用电动车骑了{power_km}公里")
            # bike = Bicycle()
            # bike.run(km - power_km)
            # 继承
            super().run(km - power_km)
ebike = EBicycle(10)
ebike.run(200)