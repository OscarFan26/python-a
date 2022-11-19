ry = 16.5825
rmb = 0.0603
none = True

while none:
	print('****************')
	print('提示：\n1.人民币兑换成日 元\n2.日 元兑换成人民币\n3.退 出 程 序')
	ask = input('请输入→→→')
	if ask == '1':
		a = int(input('您要兑换多少人民币？'))
		print(a, '元人民币可以兑换', a * ry, '日元。\n')
	elif ask == '2':
		b = int(input('您要兑换多少日元？'))
		print(b, '日元可以兑换', b * rmb, '人民币。\n')
	elif ask == '3':
		print('\n已退出程序！')
		none = False
	else:
		print('\n***************')
		print('*  输 入 错 误！*')
		print("***************\n")
