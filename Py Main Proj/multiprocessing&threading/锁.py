# encoding: utf-8 #
"""
==========
File Name:              锁                    
Author:                 Oscar Fan
Date:                   8/19/2022
requirements:                         
==========
"""
from threading import Lock, Thread

cnt = 0


def inc():
    global cnt, lock
    for i in range(999):
        lock.acquire()
        print('-START inc')
        cnt += 1
        print('-END inc:', cnt)
        lock.release()


def dec():
    global cnt, lock
    for i in range(999):
        lock.acquire()
        print('-START dec')
        cnt -= 1
        print('-END dec:', cnt)
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    t1, t2 = Thread(target=inc), Thread(target=dec)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(cnt)
