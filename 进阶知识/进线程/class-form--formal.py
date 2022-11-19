# encoding: utf-8 #
"""
==========
File Name:              class-form--formal                    
Author:                 Oscar Fan
Date:                   2022/11/19
requirements:                         
==========
"""
import threading
import time


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print('get detail html -- start')
        time.sleep(2)
        print('get detail html -- ended')


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self) -> None:
        print('get detail url -- start')
        time.sleep(4)
        print('get detail url -- ended')


if __name__ == '__main__':
    thread1 = GetDetailHtml("whatever")
    thread2 = GetDetailUrl("WHATEVER")
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('time elasped {}'.format(time.time() - start_time))
