# 	定义一个函数，函数调用以后，输出9行数据 第一行是 1 第二行12 第三行123...依此类推 第九行 123456789。
def numl(x, y):
	b = ''
	for x in range(x, y + 1):
		b += str(x)
		print(b)


start = int(input('请输入开始值：'))
end = int(input('请输入结束值：'))
numl(start, end)
print('\n程序已结束！')
