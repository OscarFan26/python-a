random.random()         # 在 [0.0, 1.0) 的左闭右开区间中产生一个随机的实数
random.uniform(a, b)    # 相当于 a + (b-a) * random.random()
random.randint(a, b)    # 在 [a, b] 的闭区间中产生一个随机的整数

# 产生特定分布的随机数
# 取决于实现方式，guass(mu, sigma) 比 normalvariate(mu, sigma) 快一些
random.gauss(mu, sigma)         # 高斯分布：以 mu 为均值，sigma 为标准差
random.normalvariate(mu, sigma) # 正态分布：以 mu 为均值，sigma 为标准差
random.lognormvariate(mu, sigma)# 对数正态分布

#对迭代器的操作
random.choices(seq)#返回的也是一个列表
random.choice(seq)                  # 从列表类型中随机选取一个元素返回
random.shuffle(seq[, random-func])  # 对 seq 进行洗牌，默认用
random.sample(seq, k)               # 从 seq 中随机选取一个子集并返回
