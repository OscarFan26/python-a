# 定义一个嵌套的列表，List = [[1,2,3,4], [2,4,6,8], [10,12,14,16]]，求这个嵌套列表的和

count = 0
List = [[1, 2, 3, 4], [2, 4, 6, 8], [10, 12, 14, 16]]
for i in range(0, 3):
	for j in range(0, 4):
		count += List[i][j]
print(count)
