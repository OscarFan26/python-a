# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/5/3 10:54
# Project name: 建党周年
# IDE: PyCharm
# File name: t1.py

import os
import sys

import tkinter as tk
from tkinter.filedialog import askopenfilename as openfile
from tkinter.filedialog import asksaveasfilename as savefile
from tkinter import messagebox as mb
import face_recognition
from PIL import Image, ImageDraw, ImageFont


class PartyBuilding:
    def __init__(self):
        self.wind = tk.Tk()
        self.wind.geometry("750x550+500+400")
        self.wind.title("main")
        self.var = tk.StringVar()
        self.address = ''

    def button2(self):
        self.address = openfile(title='Open picture', initialdir=(os.path.expanduser(r'C:\Users\yoga')),
                                filetypes=[('Picture', '*.jpeg'), ('Picture', '*.jpg'), ('Picture', '*.png')])
        path = self.address
        text = self.txt.insert('end', path)

    def face_recognition(self):
        global logo, main
        # https://cloud.tencent.com/developer/news/391041
        # Load the jpg file into a numpy array
        image = face_recognition.load_image_file(self.address)
        face_locations = face_recognition.face_locations(image)
        # A list of tuples of found face locations in css (top, right, bottom, left) order

        self.main = Image.open(self.address).convert('RGBA')
        self.logo = Image.new('RGBA', self.main.size, (0, 0, 0, 0))
        # text = '庆祝建党'
        # 引入PIL库中的模块
        draw = ImageDraw.Draw(self.logo)
        # 引入字体样式(第一个参数为字体样式，具体的可以在自己电脑中C:\Windows\Fonts下找；第二个参数为字体的大小)
        font = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', int((face_locations[0][2] - face_locations[0][0]) / 18))
        # 放置到指定位置(第一个100，代表距离图片左边距；第二个100代表距离图片顶部距离；text是定义的文字；fill设置字体颜色值;font是字体引入和大小的变量名称)
        draw.text((int((face_locations[0][1] + face_locations[0][3]) / 2), face_locations[0][0]), self.var, font=font,
                  fill=(255, 0, 0, 300))
        # logo.show()
        out = Image.alpha_composite(self.main, self.logo)
        out.show()

    def button3(self):
        saveaddr = savefile(title='Save as File',
                            filetype=[('Picture', '*.jpeg'), ('Picture', '*.jpg'), ('Picture', '*.png')])
        Image.alpha_composite(self.main, self.logo).save(saveaddr)
        mb.showinfo('OK', '保存成功！')

    def insert_point(self):
        self.var = self.column1.get()
        mb.showinfo('Message', '图片制作中...')
        self.face_recognition()

    def button4(self):
        yesno = mb.askyesno('IF EXIT', '确认退出？')
        if yesno:
            sys.exit(True)
        else:
            pass

    def about(self):
        mb.showinfo(title='ABOUT.', message='"""建党100周年纪念小程序"""\n\nMade by '
                                                   'Oscar.\t制作人：樊卓润\n\rVersion:1.0.1\t版本：1.0.1')

    def tk_run(self):
        self.column1 = tk.Entry(self.wind, show=None, font=("Lucida Fax", 18))
        self.column1.pack()
        self.column1.place(x=75, y=150)
        self.txt = tk.Text(width=50, height=2)
        self.txt.pack()
        self.txt.place(x=75, y=100)
        self.button3 = tk.Button(text='另存为图片', width=12, height=1, command=self.button3)
        self.button3.pack()
        self.button3.place(x=500, y=250)
        self.button1 = tk.Button(self.wind, text='确认输入', width=12, height=1, command=self.insert_point)
        self.button1.pack()
        self.button1.place(x=500, y=150)
        self.button2 = tk.Button(text='选择图片', width=12, height=1, command=self.button2)
        self.button2.pack()
        self.button2.place(x=500, y=100)
        self.button4 = tk.Button(text='退出', width=12, height=1, command=self.button4)
        self.button4.pack()
        self.button4.place(y=250, x=300)
        self.button5 = tk.Button(text='关于', command=self.about, height=1, width=12)
        self.button5.pack()
        self.button5.place(x=150, y=250)
        self.wind.mainloop()


if __name__ == "__main__":
    part_builting = PartyBuilding()
    part_builting.tk_run()
