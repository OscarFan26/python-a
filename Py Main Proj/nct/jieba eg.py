import jieba as j

# 精确模式
txt = """春江潮水连海平，海上明月共潮生"""
wordsa = j.lcut(txt)
print("精确模式:", len(wordsa))
print(wordsa)

# 全模式
wordsb = j.lcut(txt, cut_all=True)
print("全模式:", len(wordsb))
print(wordsb)

# 搜索模式
wordsc = j.lcut_for_search(txt)
print("搜索模式", len(wordsc))
print(wordsc)
