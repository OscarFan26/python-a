string = 'hello world'
index = string.rfind('w')
index2 = string.rfind('d')
string2 = string[index:-2]
string3 = string[index2]
print(string2 + string3)
