import random

List = []
for i in range(1000):
	s = random.randint(20, 100)
	List.append(s)
List = set(List)
print(List)
# List2 = list(List)
# List2.reverse()
# print(List2)


dic1 = {}
List1 = []
for j in range(1000):
	x = random.randint(20, 100)
	List1.append(x)
List2 = set(List1)
List1.count(j)
for y in List2:
	dic1.update({y: 0})
for z in dic1.keys():
	dic1[z] = List1.count(z)
print(dic1)
