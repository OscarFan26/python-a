# encoding=utf-8
"""
任务1 数据预处理（100分）
在做数据统计之前，需要对数据进行预处理，具体要求如下：
	读取movie_data.csv文件，以元组的形式输出行数和列数；
	删除所有有缺失值的数据行，并输出被删除的行数；
	删除所有重复行数据，并输出当前剩余的行数。
【答案】（每行30分，全正确100分）
(4924, 20)
1485
3429
"""

import pandas as pd

readcsv = pd.read_csv("movie_data.csv")
df = pd.DataFrame(readcsv)
print(df.shape)
#
#
#
dropna = df.dropna(axis=0)
print(df.shape[0] - len(dropna))
#
#
#
duplicates_of_drop = dropna.drop_duplicates()
print(duplicates_of_drop.shape[0])
