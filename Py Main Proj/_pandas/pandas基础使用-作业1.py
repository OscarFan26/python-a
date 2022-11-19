import pandas as pd

d = [chr(a) for a in range(97, 123)]
data = [d] * 26
df = pd.DataFrame(data=data, columns=[chr(A) for A in range(65, 91)],
                  index=[chr(B) for B in range(65, 91)])
print(df)

# import numpy as np
#
# b = []
# for i in range(26):
#      a = list(chr(97 + i)*26)
#      b = b + a
# c = np.array(b)
# d = c.reshape(26, 26)
# ss = pd.DataFrame(d)
# print(ss)
