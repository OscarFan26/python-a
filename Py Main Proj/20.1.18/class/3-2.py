# --*--    CODING = UTF8  --*--
# 开发团队： family FAN
# 开发时间： 2020/1/18 13:46
# 文件名称： 3-2.PY
# 开发工具： PyCharm
# --*--    wish you programming well !    --*--
flag = 1
while flag == 1:
	try:
		flag = 0
		num1 = int(input('user name:'))
		num2 = int(input('user name 2:'))

		print(num1 - num2)

	except ValueError:
		print('Please write number,not letter.')
		flag = 1
