# encoding: utf-8 #
"""
==========
File Name:              cookie                    
Author:                 Oscar Fan
Date:                   2022/6/30
requirements:                         
==========
"""
import urllib.request

cookie = '_ga=GA1.2.850994783.1654389796; gr_user_id=a8ecfd00-e3fe-4a84-baf5-4f42e9bb08bf; 87b5a3c3f1a55520_gr_last_sent_cs1=OscarFan; csrftoken=zjEsGvOkzTONmF8Ycajcorp10YDd9DHWBNkc6Bjd631BAazS4t7CXmnAxfdwiF4h; _gid=GA1.2.1424878196.1656588390; _gat=1; 87b5a3c3f1a55520_gr_session_id=3c219943-8e39-4a84-808d-7973d9b8e992; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=3c219943-8e39-4a84-808d-7973d9b8e992; 87b5a3c3f1a55520_gr_cs1=OscarFan; 87b5a3c3f1a55520_gr_session_id_3c219943-8e39-4a84-808d-7973d9b8e992=true'

url = 'https://leetcode.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'cookie': cookie,
    # referer   判断当前路径是不是由上一个路劲进来的   一般情况下  是做图片的防盗链（未登录禁止下载图片）
    'referer': 'https://www.leetcpde.com/'
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
with open('leetcode_with_cookie.txt', 'a+', encoding='utf-8') as fp:
	fp.write(content)
