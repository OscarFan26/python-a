from concurrent.futures import ThreadPoolExecutor, as_completed, FIRST_COMPLETED, wait
import time


def get_html(times):
    time.sleep(times)
    print("get page {} suc".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED)
print('main')
