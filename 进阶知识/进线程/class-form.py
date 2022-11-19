# encoding: utf-8 #
"""
==========
File Name:              class-form                    
Author:                 Oscar Fan
Date:                   2022/11/19
requirements:                         
==========
"""
import threading


class thread(threading.Thread):
    def __init__(self, target):
        super().__init__(name='MyThread')
        self.target = target

    def start(self) -> None:
        self._target = self.target
        self.run()


def test():
    for i in range(100):
        print('test')


test_t = thread(test)
test_t.start()
