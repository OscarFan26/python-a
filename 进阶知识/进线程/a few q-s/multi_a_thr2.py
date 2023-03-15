import threading
import os
import time

def work():
    res = 0
    for i in range(100000000):
        res *= i


l = []
print("本机为 {} 核CPU".format(os.cpu_count()))
time_now = time.time()
for i in range(os.cpu_count()):
    proc = threading.Thread(target=work, )
    proc.start()
    l.append(proc)
for p in l:
    p.join()
print(time.time() - time_now)

