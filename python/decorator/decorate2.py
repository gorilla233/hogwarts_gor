import time


def func1(func): #传入的是一个函数对象
    def func2(m_time):
        print("start time : ",time.strftime('%S'))
        func(m_time) #代表传入的函数被调用
        print("end time : ",time.strftime('%S'))
    return func2

@func1
def be_decorated(m_time):
    time.sleep(m_time)
    print("被装饰的函数")

be_decorated(3)

@func1
def demo2(m_time):
    time.sleep(m_time)
    print("this is a demo")

demo2(4)

# func1(be_decorated)()