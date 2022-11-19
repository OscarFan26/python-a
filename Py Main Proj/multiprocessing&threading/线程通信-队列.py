# encoding: utf-8 #
"""
==========
File Name:              线程通信-队列                    
Author:                 Oscar Fan
Date:                   8/19/2022
requirements:                         
==========
"""
import threading
import queue


class GetOperator(threading.Thread):
    def __init__(self, code: str):
        super().__init__()
        self.code = code

    def run(self):
        self.operator = self.code.split(' ')[0]
        self.code = self.code.split(' ')[1:]
        global q
        q.put(self.code)


class DealTheCode(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        global q
        self.code = q.get()
        print(f'bruh-{self.code[0]}-bruh')


if __name__ == '__main__':
    q = queue.Queue()
    # using queue (secure) because every method in
    # queue is data-secure
    code = GetOperator('test it')
    code.run()
    d = DealTheCode()
    d.run()
    del q
