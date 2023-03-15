import multiprocessing
import time
import os


def work():
    time.sleep(2)
    print("===>", file=open("tmp.txt", "w"))
    

l = []
print("本机为 {} 核CPU".format(os.cpu_count()))
time_now = time.time()
for i in range(4000):
    proc = multiprocessing.Process(target=work, )
    proc.start()
    l.append(proc)
for p in l:
    p.join()
print(time.time() - time_now)
