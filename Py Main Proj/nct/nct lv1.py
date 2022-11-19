'''
MATH
'''

# 1. abs    求绝对值
print(abs(-15.932))

# 2. sum    相加  参数：1. iterable
print(sum([2.55, 55, 300.01234]))

# 3.4. max,min  最大值/最小值
print(max([1, 2, 5, 7, 9, 0, 1, 2]))
print(min([1, 2, 5, 7, 9, 0, 1, 2]))
# 5. pow   求次方  参数：1. 一个数 2.这个数的次方
print(pow(99, 2))

# 6. round  保留数的几位小数  参数： 1.一个数 2.保留几位小数
print(round(11.111112, 5))

# 7. divmod  求一个数处以一个数的商和余数  参数 1. 被除数 2.除数
print(divmod(10, 2))

'''
convert types
'''
# 1. int  转换位整数
print(int(30.999999))

# 2. str 转换为字符串
print(str(190))

# 3. list 转换为列表
print(list((1,9, 3, 6, 'no', 'way')))

# 4. dict 转换为字典
print(dict(name=(5, 4, 6, 3)))

# 5. chr 互换ASCII码与字符串
print(chr(90))

# 6.ord 将字符串转换为ASCII码
print(ord('@'))

# 7.float 转换为小数点或浮点数
# 8.tuple 转换为元组
# 9.bool  转换为布尔类型
# 10. set 替换
# 11. range 迭代

'''
对象操作
'''

# 1. help 查看一个对象的信息或解释
# 2. type 查看类型
# 3. id  查看内存信息
# 4. len 查看对象的长度
# 5. format 格式化
# 6. dir 查看一个类型的所有方法

'''
others
'''

exec("print(1+2)")