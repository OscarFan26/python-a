s = {11, 22, 33, 44, 55, 66, 77, 88, 99, 90}
num = {}
list1 = []
list2 = []
for i in s:
	if i >= 66:
		list1.append(i)
	else:
		list2.append(i)

num.update({'key1': list1})
num.update({'key2': list2})
print(num)
