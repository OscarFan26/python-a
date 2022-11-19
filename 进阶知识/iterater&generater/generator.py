# encoding: utf-8 #
"""
==========
File Name:              generator                    
Author:                 Oscar Fan
Date:                   7/21/2022
requirements:                         
==========
"""
import dis


def count(n):
    x = 0
    while x < n:
        yield x
        x += 1


def fibo(n: int):
    last = 1
    last2 = 1
    yield 1
    yield 1
    yield 2
    for _ in range(n):
        tmp = last2
        last2 += last
        last = tmp
        yield last + last2


def yhsj():
    last_arr = [1]
    for _ in range(5):
        present_arr = [1] + [last_arr[i] + last_arr[i - 1] for i in
                             range(1, len(last_arr))] + [1]
        yield present_arr
        last_arr = present_arr


for i in yhsj():
    print(i)

l = (i for i in range(10))
print(l, type(l))


# create generator:
#       yeild func
#       seq expr([i for i in ...])

# expr send

def gen():
    for i in range(5):
        temp = yield i
        print(temp)


f = gen()
times = 0
print(next(f))
f.send(f'HelloWorld, {times}')
times += 1
print(next(f))
f.send(f'HelloWorld, {times}')
times += 1
print(next(f))
f.send(f'HelloWorld, {times}')
times += 1
print(next(f))
f.send(f'HelloWorld, {times}')
times += 1
print(next(f))
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
