# 定义一个函数，给定一个参数，整数n，判断是否是质数(prime number)（质数是只能被1和它自身整除的数）
# 如果是，返回True, 否则，返回False 。

none = True


def prime_number(n):
	a = True
	for i in range(2, n):
		if n % i == 0:
			a = False
	return a


while none:
	print('****************')
	print('提示：\n1.判断输入的数是否是素数\n2.退 出 程 序')
	ask = input('请输入→→→')
	if ask == '1':
		b = int(input('您要判断的数？'))
		c = prime_number(b)
		print(c)
	elif ask == '2':
		print('\n已退出程序！')
		none = False
	else:
		print('\n***************')
		print('*  输 入 错 误！*')
		print("***************\n")
