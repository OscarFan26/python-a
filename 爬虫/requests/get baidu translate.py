# encoding: utf-8 #
"""
==========
File Name:              get baidu translate                    
Author:                 Oscar Fan
Date:                   2022/6/1
requirements:               json          requests
==========
"""
import requests
import json


base_url = 'http://fanyi.baidu.com/sug'

kw = input('请输入要翻译的内容: ')
data = {
	'kw': kw
}
response = requests.get(base_url, params=data)
response.encoding = 'utf-8'
data = json.loads(response.text)
data_of_dict = data['data']  # list
for i in data_of_dict:
	print(i['v'])

