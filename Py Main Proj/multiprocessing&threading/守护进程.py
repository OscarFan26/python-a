# encoding: utf-8 #
"""
       * 调用foo           * foo结束 主线程不等bar，结束
         * 调用bar         * bar虽然没有执行完，但是主线程结束了，所以bar也结束了
main --------------------->>>>>>
foo    -------------------]
bar     ------------------>>>>>>
* bar是守护线程
主线程会在所有子非守护进程结束后结束（不会等守护线程，当然住线程
                                结束后所有子线程就会结束）
"""
"""
==========
File Name:              守护进程                    
Author:                 Oscar Fan
Date:                   8/19/2022
requirements:                         
==========
"""
from threading import Thread
import time


def foo():
    print('foo')
    time.sleep(1)
    print('end foo')


def bar():
    print('bar')
    time.sleep(3)
    print('end bar')


if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)
    # daemon can only be set using a constructor argument
    t2.daemon = True

    t1.start()
    t2.start()

    time.sleep(2)

    print(t1.is_alive(), t2.is_alive())
