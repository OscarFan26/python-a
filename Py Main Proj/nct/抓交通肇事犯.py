# 抓交通肇事犯
# 一辆卡车违反交通规则，撞人后逃跑。
# 现场有三人目击事件，但都没有记住车号，只记下车号的一些特征
# 甲说：牌照的前两位数字是相同的；
# 乙说：牌照的后两位数字是相同的，但与前两位不同；
# 丙是数学家，他说：四位的车号刚好是一个整数的平方。
# 请根据以上线索求出车号。

for j in range(30, 100):
    i = j**2
    i = str(i)
    if i[0] == i[1] and i[2] == i[3] and i[0] != i[2]:
       print(i)
