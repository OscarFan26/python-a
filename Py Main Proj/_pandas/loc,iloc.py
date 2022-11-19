import pandas as pd

aa = "./movie_data.csv"
r = pd.read_csv(aa)

# 某一行
# print(r.loc[5])
df = pd.DataFrame(r, index=[i for i in range(0,
                                             len(r.index))])  # dataframe数据与原csv数据在索引列差2位。
# print(df)
#
# print(df.iloc[2:6, 2:6])
# print(df.drop(index=1, inplace=True, axis=0))
# #  df.drop(columns=[;..],inplace=true/false,axis=1)
# aaaaa = df.dropna(axis=0)
# print(aaaaa)
# aaa = df["gross"]
# print(type(aaa))
# print(dir(aaa))
#
# # L--------------------------
#
# # print(aaa.mean())
# print(aaa.median())  # 3*'\n', aaa.mode())
# aaa2 = aaa.fillna(value=aaa.median())
# print(aaa2)
# print('===============')
#
# c = 0
# list_c = []
# list_i = []
# for i in df["actor_1_facebook_likes"]:
#     # print(type(i))
#     try:
#         int(i)
#     except:
#         print(c, i)
#         list_c.append(c)
#         list_i.append(i)
#
#     c = c + 1
# print(list_i)
# print(list_c)
# for r in list_c:
#     s = df.loc[r, 'movie_facebook_likes'] = aaa.median()  # 对目标表格数据进行替换
#     print(r, s)

# ====================== #
# print('============')
# 排序
# aaa3 = df["gross"].sort_values(ascending=True, inplace=False)
# print(aaa3.head(4), '\n', aaa3.tail(4))
aaa3 = df["gross"].dropna(axis=0, inplace=False)
# print(aaa3.sort_values(ascending=True, inplace=False))
# print(df["movie_facebook_likes"].dropna(axis=0, inplace=False).sort_values(ascending=True, inplace=False))
print(df[df["movie_facebook_likes"] == 0 & df["gross"] > 1950000].value_counts(
	ascending=True).sum())

# delete 重复行
# XXX.drop_duplicates()
