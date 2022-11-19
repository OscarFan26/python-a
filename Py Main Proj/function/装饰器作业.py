from functools import wraps


def decorator(func):
    """
    i am a decorator
    """

    @wraps(func)
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


@decorator
def a_function_request_dec():
    print('被装饰的函数')


print(a_function_request_dec())
print(a_function_request_dec.__name__)
print(a_function_request_dec.__doc__)

print(a())
print(a.__name__)
print(a.__doc__)
