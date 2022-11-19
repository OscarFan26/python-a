# encoding: utf-8 #
"""
==========
File Name:              review_threading                    
Author:                 Oscar Fan
Date:                   8/19/2022
requirements:                         
==========
"""
import threading
import time
import dis

cnt = 0


def add():
    global cnt
    for _ in range(1999999):
        cnt += 1


def desc():
    global cnt
    for _ in range(1999999):
        cnt -= 1


def main():
    start_time = time.time()
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # print('程序运行时间为{}'.format(time.time() - start_time))
    # print(cnt)


dis.dis(main)
