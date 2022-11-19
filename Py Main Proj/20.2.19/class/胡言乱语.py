import random

time = ['1.24,', '12.1,', '8.09,', '5.1,', '6.1,']
who = ['harry porter和', '曹操和', '诸葛亮和', '钢铁侠和', '孙悟空和']
where = ['在城堡', '在月亮', '在高速公路', '在地铁', '在公交车']
with_who = ['皮卡丘,', '李致泰,', '张馨月,', '王可欣,']
doing = ['喝下午茶', '踢足球', '打篮球', '睡觉']
end = [',他们很开心。', ',他们最喜欢这样了。']
while True:
	time_num = random.randint(0, 4)
	who_num = random.randint(0, 4)
	where_num = random.randint(0, 4)
	with_who_num = random.randint(0, 3)
	doing_num = random.randint(0, 3)
	end_num = random.randint(0, 1)
	print(time[time_num] + who[who_num] + with_who[with_who_num] + \
	      where[where_num] + doing[doing_num] + end[end_num])

	ask = input('是否继续(继续请按空格)：')
	if ask == ' ':
		continue
	else:
		break
