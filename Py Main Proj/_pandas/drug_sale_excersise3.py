'''
3 数据更新（100分）
将已经完成预处理和筛选更新后的数据，保存为新的文件。具体要求如下：
	将DataFrame类型的数据转为字典类型；
	将最新的数据保存为new_drugs_sale.json文件；
	查看new_drugs_sale.json文件的大小。
【答案】（80分）
256kb 说明：值在254kb到258kb范围内都正确
'''
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

data = drugs_sale_data.drop(["实收金额"], axis=1)
data = data.to_dict("list")
print(data)

with open("new_drug_sale.json", "w") as f:
	json.dump(data, f, ensure_ascii=False)
