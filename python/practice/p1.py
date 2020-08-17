# # print(dir())
# import sys
# import os
# # print(dir(sys))
# # print(sys.path[0])
# # print(os.listdir('./'))
# if not os.path.exists('testdir'):
#     os.mkdir('testdir')
# print(os.getcwd())
#
# import time
# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.sleep(2))

from time import sleep, ctime
import logging
#logging添加日志
import _thread
import threading
logging.basicConfig(level=logging.INFO)

loops = [2, 4]
def loop(nloop, nsec):
# def loop(nloop, nsec, lock):
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())
    # lock.release()

# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops= range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    # locks = []
    # nloops = range(len(loops))
    # for i in nloops:
    #     lock = _thread.allocate_lock()
    #     lock.acquire() #加锁
    #     locks.append(lock)
    # for i in nloops:
    #     _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # for i in nloops:
    #     while locks[i].locked(): pass
    # _thread.start_new_thread(loop0, ())
    # _thread.start_new_thread(loop1, ())
    #主线程退出后，所有子线程会全部kill掉，没有守护线程的概念
    # loop0()
    # loop1()
    # sleep(6)
    logging.info("end all at " + ctime())

if __name__ == '__main__':
    main()