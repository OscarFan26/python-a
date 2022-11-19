# encoding: utf-8 #
"""
==========
File Name:              xpath                    
Author:                 Oscar Fan
Date:                   2022/6/16
requirements:                         
==========
"""
# 爬虫: 获取网易云音乐的歌手姓名
import requests
from lxml import etree


def get_singer_name(url):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
	}
	response = requests.get(url, headers=headers)
	html = etree.HTML(response.text)
	return html.xpath('//a[@class="f-tdn"]/@title')


for i in range(65, 65+26):
	url = 'https://music.163.com/discover/artist/cat?id=2001&initial=%d' % i
	singer_name = get_singer_name(url)
	for name in singer_name:
		if name[-3:] == '的音乐':
			print(name[:-3])
		else:
			print(name[:-5])
			