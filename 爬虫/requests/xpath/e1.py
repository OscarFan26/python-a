# encoding: utf-8 #
"""
==========
File Name:              e1                    
Author:                 Oscar Fan
Date:                   2022/6/16
requirements:                         
==========
"""
# exercise1
import os, traceback
from lxml import etree
text = '''
<p>
    <ul>
        <li class="item-0"><a href="https://s1.bdstatic.com/">item 0 </a></li>
        <li class="item-1"><a href="https://s2.bdstatic.com/">item 1 </a></li>
        <li class="item-2"><a href="https://s3.bdstatic.com/">item 2 </a></li>
        <li class="item-3"><a href="https://s4.bdstatic.com/">item 3 </a></li>
        <li class="item-4"><a href="https://s5.bdstatic.com/">item 4 </a></li>
        <li class="item-5"><a href="https://s6.bdstatic.com/">item 5 </a></li>
    </ul>     
</p>
'''
html = etree.HTML(text)
# print(etree.tostring(html).decode('utf-8'))
# for i in html.xpath('/html/body/ul/li[position()<7]/a/@href'):
# 	print(i)
# for i in html.xpath('/html/body/ul/li/a['
#                     '@href="https://s4.bdstatic.com/"]/text()'):
# 	print(i)
for i in html.xpath('//a/text()'):
	print(i)
