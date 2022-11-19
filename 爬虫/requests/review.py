'''
OscarFan 制作 : 
Date: 2022-06-01 20:00:14
Have a good day forever~~~: ::python::cpp::js::html::css::bash???
'''
# encoding: utf-8 #
"""
==========
File Name:              review                    
Author:                 Oscar Fan
Date:                   2022/6/1
requirements:          requests
==========
"""
import requests

base_url = 'http://www.baidu.com'

response = requests.get(base_url)

print(response.text)
print(response.encoding)

response.encoding = 'utf-8'
print(response.text)

# with open('index.html', 'w', encoding='utf-8') as fp:
#   fp.write(response.content.decode('utf-8'))

print(response.status_code)
print(response.headers)
print(type(response.text))
print(type(response.content))
