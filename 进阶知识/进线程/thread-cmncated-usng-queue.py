# encoding: utf-8 #
"""
==========
File Name:              thread-cmncated-usng-queue                    
Author:                 Oscar Fan
Date:                   2022/11/19
requirements:                         
==========
"""
import time
from threading import *
from queue import Queue


communication_queue = Queue(maxsize=2)


def get_url():
    while True:
        print('START GET URL')
        for i in range(20):
            url = 'https://github.com/OscarFan' + str(i)
            time.sleep(0.4)
            print('URL GET COMPLETE: ' + url)
            communication_queue.put(url)
            print('URL GET  COMPLETE')


def get_data():
    while True:
        print('START GET DATA')
        for i in range(20):
            url = communication_queue.get()
            time.sleep(0.2)
            print('DATA GET COMPLETE: ' + url + ' accomplished')
            print('DATA GET  COMPLETE')


if __name__ == '__main__':
    thread1 = Thread(target=get_url)
    thread1.start()
    thread2 = Thread(target=get_data)
    for i in range(100):
        html = Thread(target=get_data)
        html.start()
        html.join()

    print('---------- end ----------')
