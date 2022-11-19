import jieba
from wordcloud import WordCloud

text = open("C:/Users/pc/Desktop/t2.txt", "r", encoding='UTF-8', errors='ignore').read()

words = jieba.lcut(text)
txt_1 = " ".join(words)
print(text)
w = WordCloud(font_path='C:/Windows/Fonts/msyhl.ttc', width=800, height=600, background_color="white")
w.generate(text)
w.to_file('ciyun.png')
 