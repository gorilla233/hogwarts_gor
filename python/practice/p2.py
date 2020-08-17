import threading
import logging
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop, nsec):
    # def loop(nloop, nsec, lock):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

loops = [2,4]
def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops= range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()

# 原语
## 锁的概念GIL
## 信号量