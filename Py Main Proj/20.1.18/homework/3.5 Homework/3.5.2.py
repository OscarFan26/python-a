# --*--    CODING = UTF8  --*--
# 开发团队： family FAN
# 开发时间： 2020/1/19 16:49
# 文件名称： 3.5.2.PY
# 开发工具： PyCharm
# --*--    wish you programming well !    --*--

saything = '华氏度摄氏度转换器'
print(saything.center(125))
say = int(input('输入一个华氏度整数：'))
transfer = 5 * (say - 32) / 9
print('摄氏度是', round(transfer))
