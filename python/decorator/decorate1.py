# 闭包函数
# 函数定义
# 1.闭包函数的定义
# def func1():
#     # 在函数内再定义一个函数
#     def func2():
#         print("我是func2")
#     # 返回“肚子"里面的函数对象
#     return func2
# # 不加括号叫做函数对象
# # 加了括号叫做函数的调用
# func22=func1()
# #func22是return的func2的函数对象
# func22()


## 作用域
def func1():
    print("我是func1")
    print(name)
    def func2():
        name = "虾米"
        print("我是func2")
        print(name)
    return func2
func1()
