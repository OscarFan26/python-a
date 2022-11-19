# encoding: utf-8 #
"""
==========
File Name:              xpath2                    
Author:                 Oscar Fan
Date:                   2022/6/30
requirements:                         
==========
"""
import requests
import lxml.etree

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

html = lxml.etree.HTML(text)
# html_data = html.xpath('//a[@href="https://s6.bdstatic.com/"]/../@class')
# print(html_data)
