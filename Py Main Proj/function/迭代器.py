l = [i for i in range(1, 1000)]
l = iter(l)  # 迭代器是一边循环一边计算
print(l)
# for i in l:
#     print(i)
print(next(l))
print(next(l))

# 生成器
t = (x for x in range(5))
print(type(t))
print(t)
print(next(t))
print(next(t))


#   ************************ #
def yield_test(n):
    for i in range(n):
        yield i
        print('第{}次循环结束'.format(i))


y = yield_test(5)
print(type(y))
print(dir(t))
print(next(y))
print(next(y))


# ******************* #
def func():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')


g = func()
print(next(g))
print(next(g))
