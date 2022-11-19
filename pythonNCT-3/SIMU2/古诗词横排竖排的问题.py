# x = input("请输入一首古诗")
poetry = "床前明月光，疑是地上霜。举头望明月，低头思故乡。"
list_1 = poetry.split("。")[:2]
list_2 = []
print(list_1)
for i in list_1:
    list_2.append(i.split('，'))

print(list_2)
for i in list_2:
    for j in i:
        print(j)

print()
print()


# 方法一：
# l2 = []
# for i in range(5):
#     l2.append(x[i::6])
# # print(l2)
# for i in l2:
#     print(i)

# 方法二：
# print(len(list_2[0][0]))
list_3 = []
for index in range(len(list_2[0][0]) ):
    s = ""
    for i in list_2:
        for j in i:
            s += j[index]
    list_3.append(s)
    
for i in list_3:
    print(i)
