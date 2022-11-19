Str = '11230143'

for i in Str:
	if i == '0':
		print(i * 2, end='')
	elif i == '1':
		print('*', end='')
	else:
		print('**' * 2, end='')
