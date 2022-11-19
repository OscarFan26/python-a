# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/5/1 14:51
# Project name: 建党周年
# IDE: PyCharm
# File name: tkinter--.py
import tkinter as tk

# 第一步，实例化object，建立一个window
window = tk.Tk()
# 第二部，给窗口可视化起名
window.title("main window")
# 第三部，设置窗口大小
window.geometry('750x550')
# 第四部，设定标签
lab = tk.Label(window, text="Hello! This is Tkinter.", bg='grey', font=('Consolas', 16), width=30, height=5)
# 第五步，放置标签
lab.pack()
# 第六部，主窗口循环显示
window.mainloop()
