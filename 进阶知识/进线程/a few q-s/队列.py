import queue
import threading
import time

q = queue.Queue(maxsize=5)


def add():
    cnt = 1
    while True:
        q.put("a")
        print("i got it")
        time.sleep(0.1)


def desc():
    while True:
        print(q.get(), "released")
        time.sleep(0.3)


a = threading.Thread(target=add)
d = threading.Thread(target=desc)
a.start()
d.start()
while True:
    time.sleep(0.175)
    print(q.qsize())
