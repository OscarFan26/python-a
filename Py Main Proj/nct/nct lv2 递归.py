# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return factorial(n-1)*n
#
# a = factorial(5)
# print(a)
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# b = fibonacci(2)
# print(b)

a = 1
def aaa():
    global  a
    a = 10
aaa()
print(a)