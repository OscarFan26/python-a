# encoding: utf-8 #
"""
==========
File Name:              计数                    
Author:                 Oscar Fan
Date:                   2021/10/26
                        
==========
"""
import random
import time

l = [random.randint(1, 99) for i in range(30)]
output_l = []
max_num = max(l)
count = [0 for xx in range(max_num + 1)]
time_now = time.time()

for i in l:
	count[i] = count[i] + 1
	print('{} value plus 1 in list--count. '.format(i))

for i in range(max_num):
	if count[i] == 0:
		print('{} is 0, pass.\n'.format(i))
		continue
	else:
		for j in range(count[i]):
			output_l.append(i)
			print('{} is append to output list.\n\t'.format(i))

print('the list before sort is {}'.format(l))
print('the list after sort is {}'.format(output_l))
print('time cost: {}'.format(time.time() - time_now))
