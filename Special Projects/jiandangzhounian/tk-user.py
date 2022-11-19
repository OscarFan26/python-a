# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/5/1 15:58
# Project name: 建党周年
# IDE: PyCharm
# File name: tk-user.py
import tkinter as tk


wind = tk.Tk()
wind.geometry("750x550")
wind.title("main")
var = tk.StringVar()
entry_user = tk.Entry(wind, show=None, font=("Lucida Fax", 18))
entry_pwd = tk.Entry(wind, show="~", font=("Lucida Fax", 18))
entry_user.pack()
entry_pwd.pack()


def correct():
    if entry_user.get() == 'oscar' and entry_pwd.get() == 'abcd1234':
        m = tk.Message(wind, text='Log in Successful', width=200)
        m.pack()
    else:
        m = tk.Message(wind, text='user name or password is wrong. Fail.',width=200)
        m.pack()

button1 = tk.Button(wind, text='confirm', width=10, command=correct)
button1.pack()

wind.mainloop()
