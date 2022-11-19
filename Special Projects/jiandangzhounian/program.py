import face_recognition
import os
import sys
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter.filedialog import askopenfilename as openfile
from tkinter.filedialog import asksaveasfilename as savefile
from tkinter import messagebox as mb

wind = tk.Tk()
wind.geometry("750x550")
wind.title("main")
var = tk.StringVar()
column1 = tk.Entry(wind, show=None, font=("Lucida Fax", 18))
column1.pack()
column1.place(x=75, y=150)
txt = tk.Text(width=50, height=2)
txt.pack()
txt.place(x=75, y=100)
address = ''


def b2():
    global address
    address = openfile(title='Open picture', initialdir=(os.path.expanduser(r'C:\Users\pc')),
                       filetypes=[('Picture', '*.jpeg'), ('Picture', '*.jpg'), ('Picture', '*.png')])
    path = address
    text = txt.insert('end', path)


def face_recg(addr):
    global logo, main

    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(addr)
    face_locations =face_recognition.face_locations(image)
    # A list of tuples of found face locations in css (top, right, bottom, left) order
    main = Image.open(addr).convert('RGBA')
    logo = Image.new('RGBA', main.size, (0, 0, 0, 0))
    # 引入PIL库中的模块
    draw = ImageDraw.Draw(logo)
    # 引入字体样式(第一个参数为字体样式，具体的可以在自己电脑中C:\Windows\Fonts下找；第二个参数为字体的大小)
    font = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', int((face_locations[0][2] - face_locations[0][0]) / 7.5))
    # 放置到指定位置(第一个100，代表距离图片左边距；第二个100代表距离图片顶部距离；text是定义的文字；fill设置字体颜色值;font是字体引入和大小的变量名称)
    draw.text((int((face_locations[0][1] + face_locations[0][3]) / 2), face_locations[0][0]), var, font=font,
              fill=(255, 0, 0, 300))
    # logo.show()
    out = Image.alpha_composite(main, logo)
    out.show()


def b3():
    saveaddr = savefile(title='Save as File',
                        filetype=[('Picture', '*.jpeg'), ('Picture', '*.jpg'), ('Picture', '*.png')])
    Image.alpha_composite(main, logo).save(saveaddr)
    mb.showinfo('OK', '保存成功！')


def insert_point():
    global var
    var = column1.get()
    mb.showinfo('Message', '制作图片中...')
    face_recg(address)





def about():
    mb.showinfo(title='ABOUT.', message='"""建党100周年纪念小程序"""\n\nMade by Oscar.\t制作人：樊卓润\n\rVersion:1.0.1\t版本：1.0.1')


button3 = tk.Button(text='另存为图片', width=12, height=1, command=b3)
button3.pack()
button3.place(x=500, y=250)
button1 = tk.Button(wind, text='确认输入', width=12, height=1, command=insert_point)
button1.pack()
button1.place(x=500, y=150)
button2 = tk.Button(text='选择图片>', width=12, height=1, command=b2)
button2.pack()
button2.place(x=500, y=100)
button4 = tk.Button(text='退出', width=12, height=1, command=b4)
button4.pack()
button4.place(y=250, x=300)
button5 = tk.Button(text='关于', command=about, height=1, width=12)
button5.pack()
button5.place(x=150, y=250)
wind.mainloop()
