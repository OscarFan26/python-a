import json as j

data = {"info":{"name":["Oscar", "Flora", "Apple", "Eric", "Hubury"], "age" : "10"},"school lasts" : {"Monday-Thursday":"15.35", "Friday" : "14.35"}}

'''
dump  {} => json
:param data: your data ==> { }
:param file: object files
:return : none
'''

with open('test.json', "w") as jsfile:
    j.dump(data, jsfile)

"""
load  json => {}
:param file: object files
:return : {...}
"""

data_empty = {}
with open("test.json", "r") as fp:
    data_empty = j.load(fp)
    print(data_empty)


"""
summarize

dump load  =>>> ' '
dumps loads ====>  " "
"""

print(type(j.dumps(data)))