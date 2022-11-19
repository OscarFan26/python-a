for i in range(1, 21):
	for x in range(1, 34):
		z = 100 - i - x
		if 5 * i + 3 * x + z / 3 == 100 and x + i + z == 100:
			print(i, x, z)
