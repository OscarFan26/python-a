from concurrent.futures import ThreadPoolExecutor
import time

def get_it(times: int, *args):
    time.sleep(times)
    print("Your args: {}".format(args))
    return times

execr = ThreadPoolExecutor(max_workers=2)
task1 = execr.submit(get_it, 2, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
task2 = execr.submit(get_it, 5, "try it")
print(task1.done())
time.sleep(2)
print(task1.done(), task2.done())
print(task1.result(), task2.result())
