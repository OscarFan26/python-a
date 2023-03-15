from concurrent.futures import ProcessPoolExecutor, as_completed
import time


def fib(n): 
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def rs(n):
    time.sleep(n)
    return n


with ProcessPoolExecutor(3) as e:
    at = [e.submit(fib, (num)) for num in range(25, 38)]
    start_time = time.time()
    for future in as_completed(at):
        data = future.result()
        print('res: {}'.format(data))
    print(time.time-start_time)


