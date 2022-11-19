# encoding: utf-8 #
"""
==========
File Name:              status_bar
Author:                 Oscar Fan
Date:                   2022/1/18
requirements:           PyQt6
==========
"""
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

"""
MainWindow 提供了主程序窗口。在其中可以创建一个具有状态栏，工具栏和经典应用程序框架
"""


class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.statusBar().showMessage("Ready.")  # 显示状态栏为Ready.
		self.setGeometry(300, 300, 400, 350)
		self.setWindowTitle("STATUS BAR")
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	m = Main()
	sys.exit(app.exec())
