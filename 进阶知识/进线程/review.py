# encoding: utf-8 #
"""
==========
File Name:              review                    
Author:                 Oscar Fan
Date:                   2022/11/19
requirements:                         
==========
"""
import threading

total: int = 0


def add():
    global total
    for i in range(1000):
        total += 1
        print("add")


def desc():
    global total
    for i in range(1000):
        total -= 1
        print('desc')


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.setDaemon(True)
thread2.setDaemon(True)
thread1.start()
thread2.start()

print(total)
