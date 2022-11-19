# encoding: utf-8 #
"""
==========
File Name:              self_made_to_use_thread                    
Author:                 Oscar Fan
Date:                   8/19/2022
requirements:                         
==========
"""
from __future__ import annotations

from threading import Thread
import time


class ThreadingA(Thread):
    def __init__(self):
        super().__init__()

    def start(self) -> None:
        super().start()

    def join(self, timeout: float | None = ...) -> None:
        self.run()

    def run(self):
        for i in range(5):
            print('A')
            time.sleep(1)
            print('A done')


class ThreadingB(Thread):
    def __init__(self):
        super().__init__()

    def start(self) -> None:
        super().start()

    def join(self, timeout: float | None = ...) -> None:
        self.run()

    def run(self):
        for i in range(5):
            print('B')
            time.sleep(1)
            print('B done')


if __name__ == '__main__':
    a, b = ThreadingA(), ThreadingB()
    a.start()
    b.start()
    # a.join()
    # b.join()
    print('---- END ----')
