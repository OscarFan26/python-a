# 有一个列表，其中包括 10 个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],要求
# 将列表中的每个元素一次向前移动一个位置，第一个元素到列表的最后，然后输出这个列表最终样式是[2,3,4,5,6,7,8,9,0,1]。
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = []
for i in range(-10, 0):
	a = list1[i + 1]
	list2.append(a)
print(list2)
