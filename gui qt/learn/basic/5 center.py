# encoding: utf-8 #
"""
==========
File Name:              5 center                    
Author:                 Oscar Fan
Date:                   2022/1/18
requirements: PyQt6
==========
"""
import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget


class Main(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setWindowTitle("5 Center")
		self.setGeometry(300, 350, 400, 300)
		self.setToolTip("A window for file '5 center'")
		self.setFont(QFont("SansSerif", 12))
		self.center()
		self.show()

	def center(self):
		qr = self.frameGeometry()  # 一个矩形窗口可以放置所有类型的窗口
		cp = self.screen().availableGeometry().center()  # 计算出分辨率和中心位置

		qr.moveCenter(cp)  # 把窗口移到屏幕中心点位置
		self.move(qr.topLeft())
		# 把应用窗口的左上方的点移到矩形窗口的左上方，这样就可以居中显示了了


if __name__ == '__main__':
	app = QApplication(sys.argv)
	m = Main()

	sys.exit(app.exec())
