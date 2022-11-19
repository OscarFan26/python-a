from PIL import ImageColor
from PIL import Image

# 请求颜色的RGBA值：ImageColor.getcolor(..., "RGBA")

r = ImageColor.getcolor("brown", "RGBA")
print(r)

# 打开image: Image.open()
ima = Image.open("C:\\Users\\pc\\Desktop\\pic2.jpeg")
print(
	ima)  # 打印  <PIL.JpegImagePlugin.JpegImageFile image mode=... size=... at ...>

# 新建image Image.new()
# Image.new(   mode = "   ",    size= ... , ...(序列),   color="   ")
new1 = Image.new("RGBA", (200, 200), "pink")
a = new1.save("new1__image_test.png")
# 没颜色： 3参数不传
new1 = Image.new("RGBA", (200, 200))
a = new1.save("new2__image_test__no_color.png")

# crop() <- 切图  粘贴 -> paste()
# 复制 -> copy()
# crop(剪切的四个坐标(用序列)
# paste(对象, 两个坐标(用序列))
pic = Image.open("C:\\Users\\pc\\Desktop\\pic3.jpg")
cropped = pic.crop((644, 210, 815, 700))
copy = pic.copy()
for i in range(10, 51000, 300):
	paste = copy.paste(cropped, (644 - i, 299))

save = copy.save("pic_test__beach_man.png")

# size()  rotate()

# try it

pic_exist = Image.open("C:\\Users\\pc\\Desktop\\pic4.jpeg")
# (w, h) = pic_exist.size
# new_pic = Image.new("RGBA", (w*60, h*60), "white")
# for i in range(100):
#     for ji in range(100):
#         paste = new_pic.paste(pic_exist, (i * w, ji * h))
#
# save_try = new_pic.save("so_many_photos__try_it_out.png")
# WHY? because the answer pic is so big! More than 3 GB!!!~

# rotate
pic_exist2 = pic_exist.copy()
pic_exist2 = pic_exist2.rotate(90)
save_rotate = pic_exist2.save("rotate_OMG.jpg")
