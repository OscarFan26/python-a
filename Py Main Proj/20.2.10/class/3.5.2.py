saything = '温度转换器'
print(saything.center(125))
say = int(input('输入一个华氏度整数：'))
transfer = 5 * (say - 32) / 9
print('摄氏度是', round(transfer))
