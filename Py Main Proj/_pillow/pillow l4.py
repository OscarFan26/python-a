import os
import PIL

# print([i for i in os.listdir("C:\\Users\\pc\\Desktop\\Py Proj\\_pillow\\") if i[-4:] == ".png"])
aa = os.listdir("C:\\Users\\pc\\Desktop\\Py Proj\\_pillow\\")
# for i in aa:
#     if i[-4:] == ".png":
#         print(i, "\n\n")

memory_num = 0
a = 0
competitive_num = 0
for j in aa:
	a = os.path.getsize("C:\\Users\\pc\\Desktop\\Py Proj\\_pillow\\" + j)
	if competitive_num < a:
		memory_num = a

print(memory_num)
