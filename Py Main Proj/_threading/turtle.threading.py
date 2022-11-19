import time, threading

total = 0


def add():
	global total
	time.sleep(2)
	for i in range(200):
		total += 1
	print('add.print')


def desc():
	global total
	time.sleep(2 * 2)
	for i in range(200):
		total -= 1
	print('desc.print')


start_time = time.time()
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

# thread1.setDaemon(True)  # 守护线程
# thread2.setDaemon(True)  # 守护线程:子线程设置成守护线程之后，主线程自动结束
thread1.start()
thread2.start()
# thread1.join()
# thread2.join()


print('程序运行时间为{}'.format(time.time() - start_time))
print(total)
