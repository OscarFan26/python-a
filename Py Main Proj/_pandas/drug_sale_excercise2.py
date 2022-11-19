"""
任务2 数据统计（100分）
对处理好的数据进行统计，具体要求如下：
	按照销售数量对数据行进行降序排序；
	找出销量前三的药品，添加到列表中，并输出列表；
	找出销量倒数前三的的药品，添加到列表中，并输出列表；
	计算实收金额这一列数据的中位数、平均值（保留2位小数）、总数，并输出。任务
【答案】（每行15分，全正确80分）
['缬沙坦氢氯噻嗪片(复代文)', '吲达帕胺片(寿比山)', '苯磺酸氨氯地平片(络活喜)']
['缬沙坦胶囊(代文)', '尼群地平片', '厄贝沙坦片(安博维)']
26.5
46.48
299014.26
"""
import pandas as pd
import json

drugs_sale_data1 = pd.read_csv("drugs_sale_data1.csv")
drugs_sale_data2 = pd.read_csv("drugs_sale_data2.csv")

drugs_sale_data1 = drugs_sale_data1.dropna()
drugs_sale_data2 = drugs_sale_data2.dropna()

drugs_sale_data = pd.concat([drugs_sale_data1, drugs_sale_data2], axis=0)
rows = drugs_sale_data.shape[0]
print(rows)

drugs_sale_data = drugs_sale_data.drop(["订单号", "商品编码"], axis=1)

drugs_sale_data = drugs_sale_data.sort_values(ascending=False, by="销售数量")
sort_high = []
sort_low = []

for i in drugs_sale_data["商品名称"].head(3):
	sort_high.append(i)
print(sort_high)
for i in drugs_sale_data["商品名称"].tail(3):
	sort_low.append(i)
print(sort_low)

print(drugs_sale_data["实收金额"].median(), "\n",
      round(drugs_sale_data["实收金额"].mean(), 2), "\n",
      drugs_sale_data["实收金额"].sum())
