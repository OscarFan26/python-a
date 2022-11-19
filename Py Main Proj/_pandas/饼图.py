import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.unicode.east_asian_width', True)
date = [i for i in range(1, 16)]
# date = [7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 7.10, 7.11, 7.12, 7.13, 7.14, 7.15]
# sports = [3, 2, 1, 5, 1, 4, 1, 3, 1, 2, 5, 1, 4, 1, 3]
# sports = ['游泳', '跑步', '跳绳', '俯卧撑', '跳绳', '羽毛球', '跳绳', '游泳', '跳绳', '跑步', '俯卧撑', '跳绳', '羽毛球', '跳绳', '游泳']
sports = ['游泳', '跑步', '跳绳', '羽毛球', '俯卧撑']
# duration = [60, 30, 20, 15, 20, 120, 20, 60, 20, 30, 15, 20, 120, 20, 60]
duration = [180, 60, 120, 240, 30]
# types = ['跳绳', '跑步', '游泳', '羽毛球', '俯卧撑']
# columns = ['date', 'sports', 'duration']

# data = list(zip(date, sports, duration))
# df = pd.DataFrame(data=data, columns=columns, index=sports)
# print(df)

# x = date
# y = duration
# plt.plot(x, y, marker='o')
# plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10, 10))
# label = df['sports']
# sizes = df['']
# colors = ['red', 'yellow', 'slateblue', 'green', 'magenta', 'cyan', 'darkorange', 'lawngreen']
plt.pie(x=duration,
        labels=sports,
        labeldistance=0.8,
        autopct='%.1f%%',
        startangle=0,
        explode=(0.2, 0, 0, 0, 0),
        shadow=True,
        wedgeprops={'width': 0.4, 'edgecolor': 'k'},
        # radius=2,
        center=(0.2, 0.2),
        textprops={'fontsize': 12, 'color': 'k'},
        pctdistance=0.7)
plt.axis('equal')
plt.title('暑期各类运动项目时间占比图')
plt.show()
