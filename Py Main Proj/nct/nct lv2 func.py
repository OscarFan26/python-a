def add(*num):
    s = 0
    for i in num:
        s += i
    print(s)


add(3, 4, 5)


def add2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


add2(name="Oscar")




