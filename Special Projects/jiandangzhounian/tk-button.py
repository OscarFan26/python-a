# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/5/1 15:09
# Project name: 建党周年
# IDE: PyCharm
# File name: tk-button.py
import tkinter as tk
#
#
wind = tk.Tk()
wind.geometry("750x550")
wind.title("main")
var = tk.StringVar()
lab = tk.Label(wind, textvariable=var, bg="grey", font=("Lucida Fax", 13), width=130, height=2)
lab.pack()

# < --------------------------------------------- >
# on_hit = False
#
#
# def click_me_my_button():
#     global on_hit
#     if not on_hit:
#         on_hit = True
#         var.set("you hit the button")
#     else:
#         on_hit = False
#         var.set('-- you has hitten the button -> stand by --')

#
# button1 = tk.Button(wind, text="a button", font=("Lucida Fax", 18), width=12, height=3, command=click_me_my_button)
# button1.pack()
entry_user = tk.Entry(wind, show=None, font=("Lucida Fax", 18))
entry_pwd = tk.Entry(wind, show="*", font=("Lucida Fax", 18))

entry_user.pack()
entry_pwd.pack()
# < ------------------------------------------->
def insert_point():
    var = entry_user.get()
    txt.insert('end', var)


def insert_end():
    var = entry_pwd.get()
    txt2.insert('end', var)


button1 = tk.Button(wind, text='insert point', width = 10, height=2, command=insert_point)
button2 = tk.Button(wind, text='insert end', width = 10, height=2, command=insert_end)

button1.pack()
button2.pack()
button1.place(x=200, y=200)
button2.place(x=300, y=200)

txt = tk.Text(wind, height=3)
txt2 = tk.Text(wind, height=3)
txt.pack()
txt2.pack()
wind.mainloop()