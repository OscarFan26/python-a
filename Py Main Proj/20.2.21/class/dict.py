print(dir({}))
dic = {'clear': '删除', 'copy': '复制', 'fromkeys': '来自关键字', 'get': '获取',
       'items': '项目', 'keys': '关键字', 'pop': '删除', 'popitem': '删除最后一组',
       'setdefault': '设置默认值', 'update': '更新', 'values': '值'}
for k, v in dic.items():
	print(k, ":", v)
# 删除
dic.pop("pop")
print(dic)
dic.popitem()
print(dic)
# 查找
print(dic.get("copy"))
print(dic.get("jjj"))
'items'
'keys'
'values'
# 增加
dic.update({"up": '向上'})
print(dic)
dic.setdefault('date', '日期')
print(dic)
# 新建列表
new_dic = dict.fromkeys([str(i) for i in range(5)], 'haha')
print(new_dic)
# 复制
'copy'
# 生成26个大写字母
print([chr(i) for i in range(65, 90)])
