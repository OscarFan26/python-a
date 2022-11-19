import urllib.parse
import urllib.request
from lxml import etree
import time
import json

item_list = []


def handle_request(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    # 拼接url
    # url=url % page
    url = url.format(page)
    return urllib.request.Request(url=url, headers=headers)


def parse_content(content):
    # 生成对象
    tree = etree.HTML(content)
    # 抓取内容
    li_list = tree.xpath('//li[@class="article-summary"]')
    for lt in li_list:
        title = lt.xpath('.//span[@class="article-title"]/a/text()')[0]
        content = lt.xpath('.//div[@class="summary-text"]/p/text()')
        for i in range(len(content)):
            content[i] = content[i].replace('\n', '').replace('\r', '').replace(
                '\t', '')
        text = '\n'.join(content)
        item = {
            '标题': title,
            '内容': text,
        }
        item_list.append(item)


def main():
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    url = 'http://xiaohua.zol.com.cn/new/{}.html'
    # http://xiaohua.zol.com.cn/new/2.html
    for page in range(start_page, end_page + 1):
        # 构建请求对象
        print(f'正在爬取采集第{page}页............')
        request = handle_request(url, page)
        content = urllib.request.urlopen(request).read().decode('gbk')
        # 解析内容
        parse_content(content)
        print(f'完成第{page}页数据采集............')
        # string=json.dumps(item_list,ensure_ascii=False)
        with open('xiaohua.txt', 'w+', encoding='utf-8') as fp:
            # fp.write(string)
            fp.write(str(item_list))


if __name__ == '__main__':
    main()
