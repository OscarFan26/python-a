#  若一个口袋中放有24个球，其中有12个红的。3个白的和9个黒的，问从中任取13个共有多少种不同的颜色搭配？

count = 0
for red in range(1, 13):
	for black in range(1, 10):
		for white in range(1, 4):
			if red + white + black == 13:
				count += 1
print(count)
