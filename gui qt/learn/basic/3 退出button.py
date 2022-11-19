# encoding: utf-8 #
"""
==========
File Name:              3 退出button                    
Author:                 Oscar Fan
Date:                   2022/1/9
requirements:    PyQt6
==========
"""
# 接下来，只有新的代码我才写注释哦
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont


class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setWindowTitle('Only an exit button and some tool tips')
		self.setToolTip('Exercise for <b>exit button</b>.')
		self.setFont(QFont('SansSerif', 13))
		self.resize(600, 450)
		self.move(100, 100)

		button = QPushButton('Exit', self)
		button.resize(button.sizeHint())
		button.move(50, 40)
		button.setToolTip(
			'Click <i>exit</i> button to <b>exit</b> this program')
		button.clicked.connect(QApplication.instance().exit)  # 这样只要一按就会退出，这里是绑定

		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())
