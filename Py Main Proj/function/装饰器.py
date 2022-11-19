from functools import wraps

# 函数的参数可以是函数

def my_map(func, iterable):
    l = []
    for i in iterable:
        l.append(func(i))
    return l


print(my_map(abs, [1, -1]))


def my_filter(func, iterable):
    l = []
    for x in iterable:
        if func(x):
            l.append(x)
    print(l)


my_filter(lambda x: x % 2 == 0, [10, 20, 30, 11, 13, 15, True])


# 函数里面可以定义参数(嵌套函数)
# 函数可以作为参数结果return
def first(n):
    print(n)

    def second():
        print('second')
        return 'second'

    second()
    return second


first(10)()


def decorator(func):
    '''
    i am a decorator
    '''

    def wrap():
        print('-----------')
        func()
        print('-----------')

    return wrap


@decorator
def a():
    '''
    i am 'a'
    '''
    pass


def a_function_request_dec():
    print('被装饰的函数')


a_function_request_dec()
a()


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return 'func won\'t run'
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return 'func is running'


can_run = True
print(func())

print(func.__name__)
print(func.__doc__)
