import pandas as pd

series = pd.Series([i for i in range(20)])
print(series)
print('\n\n\n\n\n' * 5)
series2 = pd.Series(
	{'age': '10', 'name': 'Oscar', 'school': 'x1zx', 'class': '3-4', 'No.': 26})
print(series2)

series3 = pd.Series([chr(a) for a in range(97, 123)],
                    [chr(b) for b in range(65, 91)])
print(series3)
print('\n\n\n\n\n' * 2)

aaaa = '\n\n\n'
print(series.values, aaaa)
print(series.index)
series.name = 'Oscar'
print(series.name)
print(series3[['A', 'B', 'G']])
print(series3['K':'Z'])
