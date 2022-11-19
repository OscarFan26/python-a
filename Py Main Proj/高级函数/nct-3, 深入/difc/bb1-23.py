#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2021/8/21
# File name : bb1-23
"""
Q: 请将下列二维列表转换成下面的字典
List_1=[["海", "日", "生","残","夜"],[" 江", "春", "入","旧","年"]]
List_2=[["乡", "书", "何","处","达"],[" 归", "雁", "洛","阳","边"]]
输出格式：
{"颈联":"海日生残夜，江春入旧年。","尾联":"乡书何处达， 归雁洛阳边。"}
"""
List_1 = [["海", "日", "生", "残", "夜"],
          [" 江", "春", "入", "旧", "年"]]
List_2 = [["乡", "书", "何", "处", "达"],
          [" 归", "雁", "洛", "阳", "边"]]
dic = {}
s = ""
s2 = ""

for i in range(len(List_1)):
    if i % 2 == 0:
        s = s + "".join(List_1[i]) + "，"
    else:
        s = s + "".join(List_1[i]) + "。"
for j in range(len(List_2)):
    if j % 2 == 0:
        s2 = s2 + "".join(List_2[j]) + "，"
    else:
        s2 = s2 + "".join(List_2[j]) + "。"

dic.update({"颈联": s, "尾联": s2})
print(dic)
