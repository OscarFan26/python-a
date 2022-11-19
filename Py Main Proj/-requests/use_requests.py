import requests
from PIL import Image

pic = 'favicon.ico'
r = requests.get('http://github.com/favicon.ico').content
with open(pic, 'wb') as fp:
	fp.write(r)
im = Image.open(pic)
im.show()

# r1 = requests.get('http://play.baobao88.com/vbaobao88/vid-da2d42860ccad8c78f3c7abd93dcad3b/bbfile/media/000003/%E6%96%87%E8%89%BA/%E5%9B%BD%E6%AD%8C%E4%BC%B4%E5%A5%8F/90191b13.mp3').content
# with open('demo1.mp3', 'wb') as fp1:
#     fp1.write(r1)


# r2 = requests.get('http://x1zx.xhedu.sh.cn/cms/data/templates/images/index/2014-02-27_15-18-22_0.jpg').content
# with open('一中心图片.jpg', 'wb') as fp2:
#     fp2.write(r2)
# im = Image.open('一中心图片.jpg')
# im.show()
