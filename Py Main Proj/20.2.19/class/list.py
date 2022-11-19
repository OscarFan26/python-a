l = [i for i in range(10)]
# 增加
print(l)
l.append("append")
print(l)
l.insert(5, "insert")
print(l)
l.extend(["ext", "end"])
print(l)
# 删除
l.pop()
print(l)
l.remove("insert")
print(l)
l.clear()
print(l)

l = [i for i in range(10)]
# 查找
ind = l.index(5)
print(ind)
cou = l.count(5)
print(cou)
# 其他
ll = l.copy()
print(ll)
l.reverse()
print(l)
l.sort()
print(l)
