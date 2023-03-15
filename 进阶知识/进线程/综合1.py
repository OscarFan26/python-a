import requests
import lxml

req = requests.get("https://www.kanunu8.com/book2/11138/213902.html")
t = req.content.decode(encoding="gbk")
print(t)
