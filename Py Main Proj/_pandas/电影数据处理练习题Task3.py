import pandas as pd

rdcsv = pd.read_csv("movie_data.csv")

a = rdcsv[(rdcsv["gross"] > 50000000) & (rdcsv["budget"] < 100000000)]
print(a["gross"].max())
print(a["budget"].min())
#
#
#
sort = rdcsv["imdb_score"].sort_values(ascending=True)
aa = []
for i in a.head()["gross"]:
	aa.append(i)
print(aa)

"""
任务3 数据更新（100分）
将已经完成预处理和筛选更新后的数据，保存为新的文件。具体要求如下：
	找出所有以actor开头的字段名，并添加到列表中；
	删除所有以actor开头的数据列；
	将最新的数据保存为new_movie_data.csv文件；
	查看new_movie_data.csv文件的大小。
【答案】（100分）
116kb 说明：值在114 kb到118kb范围内都正确

"""
actor = []
for j in a["actor"]:
	actor.append(j)
a.drop(axis=0, columns=["actor"])
