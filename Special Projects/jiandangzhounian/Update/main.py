#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time : 2021/9/4
# File name : main

import face_recognition
import os
import sys
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter.filedialog import askopenfilename as openfile
from tkinter.filedialog import asksaveasfilename as savefile
from tkinter import messagebox as mb

window = tk.Tk()
window.geometry("525x300")
window.title("main")
window.resizable(0, 0)
window.configure(bg='grey')
var = tk.StringVar()
var.set('____' * 5)


def button_about():
    mb.showinfo(title='ABOUT.',
                message='建党100周年修图小程序\n\nMade by Oscar.\t制作人:樊卓润\n\rVersion:1.1.2\t版本:1.1.2')


def button_save():
    saveaddr = savefile(title='Save as File',
                        filetype=[('Picture', '*.png')])
    Image.alpha_composite(main, logo).save(saveaddr)
    mb.showinfo('OK', '保存成功！')


def button_exit():
    yesno = mb.askyesno('IF EXIT', '确认退出？')
    if yesno:
        sys.exit(True)
    else:
        pass


def button_open():
    global address
    address = openfile(title='Open picture', initialdir=(os.path.expanduser(r'C:\Users\pc')),
                       filetypes=[('Picture', '*.jpeg'), ('Picture', '*.jpg'), ('Picture', '*.png')])
    path = address
    var.set(path)


def face_recg(addresses, input_text):
    global logo, main
    l = len(input_text)
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(addresses)
    face_locations = face_recognition.face_locations(image)
    # A list of tuples of found face locations in css (top, right, bottom, left) order
    main = Image.open(addresses).convert('RGBA')
    logo = Image.new('RGBA', main.size, (0, 0, 0, 0))
    # 引入PIL库中的模块
    draw = ImageDraw.Draw(logo)
    # 引入字体样式(第一个参数为字体样式，具体的可以在自己电脑中C:\Windows\Fonts下找；第二个参数为字体的大小)
    font = ImageFont.truetype(r'C:/Windows/Fonts/msyh.ttc', int((face_locations[0][2] - face_locations[0][0]) / 14))
    #
    # font_graph = Image.new('RGBA', (100,
    #                                 int((face_locations[0][2] - face_locations[0][0]) / 14)), (255, 255, 255, 255))
    # draw_font = ImageDraw.Draw(font_graph)
    # draw_font.text((0, 0), input_text, font=font, fill=(255, 0, 0, 300))
    # font_graph.show()
    # 放置到指定位置(第一个100，代表距离图片左边距；第二个100代表距离图片顶部距离；text是定义的文字；fill设置字体颜色值;font是字体引入和大小的变量名称)
    draw.text((int((face_locations[0][1] + face_locations[0][3]) / 2 - (
                face_locations[0][1] - face_locations[0][3]) / 3.5), face_locations[0][0]), input_text, font=font,
              fill=(255, 0, 0, 300))
    # logo.show()
    out = Image.alpha_composite(main, logo)
    out.show()


def run_program():
    # global var1
    var1 = column1.get()
    length = len(var1)
    mb.showinfo('Message', '制作图片中...')
    face_recg(address, var1)


def button_how_to_use():
    txt_to_use = '使用指南：\n\n\n' \
                 '① 点击选择图片，可以选择你需要修图的图片(格式为.jpg .jpeg .png)\n' \
                 '② 在输入栏中输入你想要贴的文字，完成后并点击‘确认输入’\n' \
                 '③ 在出来的提示框中点击‘确定’，图片马上就会显示出来了\n' \
                 '④ 关闭图片后，点击‘另存为图片’可以选择保存名称与格式(注意:由于格式问题，目前只支持 *.png 格式，请谅解!\n' \
                 '⑤ 点击‘关于’可以显示简介，点击‘退出’即可退出此程序\n'

    how_window = tk.Tk()
    how_window.geometry('700x375+100+100')
    how_window.title('我应该如何使用？')
    how_window.resizable(0, 0)
    how_to_use_message.place(x=20, y=10)
    button_exit_how = tk.Button(how_window, text='退出此窗口', width=12, height=1,
                                command=how_window.destroy)

    button_exit_how.place(x=20, y=300)
    # mainloop
    how_window.mainloop()


# widget
welcome_label = tk.Label(window, text='欢迎来到建党100周年修图小程序', font=('隶书', 20),
                         foreground='orange', background='grey')
welcome_label.place(x=50, y=10)
# Entry
column1 = tk.Entry(window, show=None, font=("Lucida Fax", 18), foreground='orange', background='grey',
                   )
column1.place(x=55, y=130)
# message
txt_message = tk.Message(window, textvariable=var, width=300, foreground='brown', background='grey',
                         font=('Microsoft YaHei', 10))
txt_message.place(x=55, y=80)
# button
address = ''
button1 = tk.Button(window, text='确认输入', width=12, height=1, command=run_program, foreground='green')
button1.place(x=380, y=130)
button2 = tk.Button(text='选择图片>', width=12, height=1, command=button_open, foreground='green')
button2.place(x=380, y=80)
button3 = tk.Button(text='另存为图片', width=12, height=1, command=button_save, foreground='green')
button3.place(x=380, y=180)
button4 = tk.Button(text='退出', width=12, height=1, command=button_exit, foreground='green')
button4.place(x=205, y=230)
button5 = tk.Button(text='关于', height=1, width=12, command=button_about, foreground='green')
button5.place(x=55, y=230)
button6 = tk.Button(window, text='如何使用？', width=12, height=1, command=button_how_to_use, foreground='green')
button6.place(x=380, y=230)

# mainloop
window.mainloop()
