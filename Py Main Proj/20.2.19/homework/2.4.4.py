# 定义一个嵌套的列表，List = [[1,2,3,4], [2,4,6,8], [10,12,14,16]]，求这个嵌套列表的平均数

count = 0
List = [[1, 2, 3, 4], [2, 4, 6, 8], [10, 12, 14, 16]]
for i in List:
	for j in i:
		count += j

total = 0
for f in range(len(List)):
	total += len(List[f])
print(round(count / total, 2))
