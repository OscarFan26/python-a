# encoding=utf-8
'''
任务2 数据统计（100分）
对处理好的数据进行统计，具体要求如下：
	筛选出总收入大于50000000并且支出小于100000000的数据行；
	输出筛选出的电影中总收入gross字段最高的数值；
	输出筛选出的电影中支出budget字段最低的数值；
	对筛选出的数据行按照imbd_score值的大小进行降序排序；
	将排序好的前五行数据中的gross值添加到列表中，并输出列表。

【答案】（每行30分，全正确100分）
623279547.0
60000.0
[84185387.0, 214948780.0, 50800000.0, 100614858.0, 52200504.0]
'''
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
