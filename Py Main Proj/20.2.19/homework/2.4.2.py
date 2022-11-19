# 定义一个嵌套的列表，List = [[1,2,3,4], [2,4,6,8], [10,12,14,16]]
# 求这个嵌套列表的最大值、最小值
# list_a = [[1, 2, 3, 4], [2, 4, 6, 8], [10, 12, 14, 16]]
# newlist = []
# newlist2 = []
# Min = 0
# for i in range(0,3):
#     j = max(list_a[i])
#     newlist.append(j)
#     k = min(list_a[i])
#     newlist2.append(k)
# print(max(newlist), min(newlist2))

list_a = [[1, 2, 3, 4], [2, 4, 6, 8], [10, 12, 14, 16]]
minnum = 999
maxnum = 0
for i in list_a:
	for j in i:
		if j > maxnum:
			maxnum = j
		if j < minnum:
			minnum = j

print(maxnum, minnum)
