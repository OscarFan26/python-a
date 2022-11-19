"""
任务1 数据预处理（100分）
在做数据统计之需要对数据进行预处理，具体要求如下：
	分别删除drugs_sale_data1.csv和 drugs_sale_data2.csv中所有有缺失值的数据行；
	将删除缺失值后的2个数据合并为一个数据，并输出合并后的行数；
	删除订单号和商品编码这2个无关列。
【答案】（80分）
6433
"""
import json
import pandas as pd

aa_data1 = pd.read_csv("drugs_sale_data1.csv")
aa_data2 = pd.read_csv("drugs_sale_data2.csv")

dropna_data1 = aa_data1.dropna(inplace=False)
dropna_data2 = aa_data2.dropna(inplace=False)

concat = pd.concat([dropna_data2, dropna_data1], axis=0)
print(len(concat))

drugs_sale_data = concat.drop(["订单号", "商品编码"], axis=1)
data = drugs_sale_data.to_dict()

# print(drugs_sale_data)
with open("new_drug_sale.json", "w") as f:
	json.dump(data, f, ensure_ascii=False)
