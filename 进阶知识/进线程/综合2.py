import requests
from lxml import etree


def gernerate_base_url():
    req = requests.get('https://www.kanunu8.com/files/sf/')
    text = req.text.encode('iso-8859-1').decode('gbk')
    # type: ignore
    return etree.HTML(text).xpath('//a[@target="_blank"]/@href')


# def work(url):
#      f =  lambda i : "https://www.kanunu8.com/book2/11138/2139{}.html".format(i)
#     req = requests.get(f(i))
#     t = req.content.decode(encoding="gbk")
#     html = etree.HTML(t) # type: ignore
#     things = html.xpath("//div[@class='text']/p[position()>1]/text()")
#     # 处理这个数据
#     txt: str = ""
#     for thing in things:
#         txt += thing.replace("\\xa0"*4, "\t").replace("\\u3000", "").replace("\\r\\n", "")
#     return [int(i)-1, f"{'第{}章'.format(int(i)-1)}\n{txt}\n\n"]


def test_work(url):
    req = requests.get(url)
    text = req.text.encode('iso-8859-1').decode('gbk')
    # type: ignore
    return etree.HTML(text).xpath('//tr[position()=4]/td//table//a/@href')


url = gernerate_base_url()
# test1
url = "https://www.kanunu8.com/" + url[0]
print(test_work(url))
