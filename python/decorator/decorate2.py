def func1(func): #传入的是一个函数对象
    def func2():
        func() #代表传入的函数被调用
        print("我是func2")
    return func2

@func1
def be_decorated():
    print("被装饰的函数")

be_decorated()
# func1(be_decorated)()