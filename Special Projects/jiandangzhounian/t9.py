import face_recognition
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk

wind = tk.Tk()
wind.geometry("750x550")
wind.title("main")
var = tk.StringVar()
entry_column = tk.Entry(wind, show=None, font=("Lucida Fax", 18))
entry_column.pack()


def insert_point():
    global var
    var = entry_column.get()
    
    
button1 = tk.Button(wind, text='确认输入', width=10, height=2, command=insert_point)
button1.pack()


wind.mainloop()



# https://cloud.tencent.com/developer/news/391041
# Load the jpg file into a numpy array
image = face_recognition.load_image_file("face.jpeg")
face_locations = face_recognition.face_locations(image)
# A list of tuples of found face locations in css (top, right, bottom, left) order

main = Image.open(r"face.jpeg").convert('RGBA')
logo = Image.new('RGBA', main.size, (0, 0, 0, 0))
# text = '庆祝建党'
# 引入PIL库中的模块
draw = ImageDraw.Draw(logo)
# 引入字体样式(第一个参数为字体样式，具体的可以在自己电脑中C:\Windows\Fonts下找；第二个参数为字体的大小)
font = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', int((face_locations[0][2] - face_locations[0][0]) / 18))
# 放置到指定位置(第一个100，代表距离图片左边距；第二个100代表距离图片顶部距离；text是定义的文字；fill设置字体颜色值;font是字体引入和大小的变量名称)
draw.text((int((face_locations[0][1] + face_locations[0][3]) / 2), face_locations[0][0]), var, font=font, fill=(255, 0, 0, 300))
# logo.show()
out = Image.alpha_composite(main, logo)
out.show()
