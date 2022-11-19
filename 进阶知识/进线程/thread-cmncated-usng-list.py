# encoding: utf-8 #
"""
==========
File Name:              thread-cmncated-usng-queue                    
Author:                 Oscar Fan
Date:                   2022/11/19
requirements:                         
==========
"""
import threading
from threading import RLock
import time


communication_queue = []
lock = RLock()


def get_url():
    global communication_queue
    while True:
        print('get url started')
        lock.acquire()
        time.sleep(0.4)
        for i in range(20):
            communication_queue.append("https://projectsedu.com/{id}".format(
                id=1))
        print('XXX', communication_queue[0])
        print('get url finished')
        lock.release()


def get_data():
    global communication_queue
    while True:
        for i in range(20):
            if len(communication_queue):
                lock.acquire()
                print('get data started')
                url = communication_queue.pop()
                time.sleep(0.2)
                url += '\tfinished reading'
                print(url)
                print('get data finished')
                lock.release()


if __name__ == '__main__':

    thread1 = threading.Thread(target=get_url)
    thread1.start()
    thread2 = threading.Thread(target=get_data)
    for i in range(100):
        html = threading.Thread(target=get_data)
        html.start()
        html.join()

    print('---------- end ----------')

