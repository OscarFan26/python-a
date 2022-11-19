def fun_sum(first, last):
	cou = 0
	for i in range(first, last + 1):
		cou += i
	return cou


result = fun_sum(1, 100)
print(result)
