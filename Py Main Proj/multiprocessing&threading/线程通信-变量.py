# encoding: utf-8 #
"""
==========
File Name:              线程通信                    
Author:                 Oscar Fan
Date:                   8/19/2022
requirements:                         
==========
"""
import threading


class GetOperator(threading.Thread):
    def __init__(self, code: str):
        super().__init__()
        self.code = code

    def run(self) -> None:
        self.operator = self.code.split(' ')[0]
        self.code = self.code.split(' ')[1:]
        global const
        const = self.code


class DealTheCode(threading.Thread):
    def __init__(self, usable_code: str):
        super().__init__()
        self.code = usable_code

    def run(self) -> None:
        print(f'bruh-{self.code}-bruh')


if __name__ == '__main__':
    # using variable (unsecure)
    const: str = ''
    t1 = GetOperator('test the code')
    t1.run()
    t2 = DealTheCode(const)
    t2.run()
