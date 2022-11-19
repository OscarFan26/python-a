import pandas as pd

aa = "./movie_data.csv"
read = pd.read_csv(aa)
# read.to_csv("movie_record.csv")
# print(read.head(10),read.tail(20))
print(read[10:15], read["genres"], read[:1], read[10:],
      read[["genres", "language"]], read[:3][["genres", "language"]])
