# --*--    CODING = UTF8  --*--
# 开发团队： family FAN
# 开发时间： 2020/2/13 21:31
# 文件名称： 2.2.3.PY
# 开发工具： PyCharm
# --*--    wish you programming well !    --*--
#  制作一张10*10的乘法表

for i in range(1, 11):
	for j in range(1, i + 1):
		print(str(j) + '*' + str(i) + '=' + str(j * i) + '\t', end='')
	print('')
