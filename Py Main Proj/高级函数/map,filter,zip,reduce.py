
l = [1, 2, 3, 4]
print(list(map(lambda x: x ** 2 + 1, l)))

# ******************************** #

l_a = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, l_a)))

# ******************************** #
from functools import reduce

a = lambda x, y: x * y
print(reduce(a, range(1, 101)))

# ******************************** #
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
print(list(zip(l_1, l_2)))
l_3 = [7, 8, 9]
print(list(zip(l_1, l_2, l_3)))
print(dict(zip('abc', [1, 2, 3])))
# ************* #


def a(*n):
    for i in n:
        print(i)


a(1, 2, 3)
a(*(1, 2, 3))
a((1, 2, 3))
