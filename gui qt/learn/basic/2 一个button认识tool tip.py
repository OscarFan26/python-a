# encoding: utf-8 #
"""
==========
File Name:              2 一个button认识tool tip
Author:                 Oscar Fan
Date:                   2022/1/9
                        
==========
requirements: pyqt6==6.0.3
"""
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont


class Example(QWidget):  # 创建类， 一定要继承QWidget
	def __init__(self):  # 初始化一下
		super().__init__()  # 继承接受

		self.initUI()  # 调用方法initUI

	def initUI(self):
		self.resize(500, 350)  # 定义大小
		self.move(100, 50)  # 把窗口移动到x 100 y 50的位置
		self.setWindowTitle(
			'A button and some tool tips, including font')  # 设置标题
		self.setFont(QFont('Consolas', 13))  # 设置字体
		self.setToolTip(
			'Exercise of <b><i><u>button<u/> and <u>tool tip </u>.</b></i>')  # 一个tool tip

		button = QPushButton('A button', self)  # 定义一个push button
		button.move(30, 50)  # 移动到30, 50位置
		button.resize(button.sizeHint())  # 大小为系统推荐大小
		button.setToolTip('Only a button, don\'t <b>worry</b>.')

		self.show()  # 显示主窗口


if __name__ == '__main__':  # 这部分跟 *1.py 大同小异， 应该可以理解
	app = QApplication(sys.argv)
	ex = Example()  # 实例化
	sys.exit(app.exec())
