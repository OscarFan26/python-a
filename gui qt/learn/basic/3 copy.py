# encoding: utf-8 #
"""
==========
File Name:              3 copy                    
Author:                 Oscar Fan
Date:                   2022/1/14
requirements:                         
==========
"""
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont


class Main(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setWindowTitle('Only an exit button and some toll tips')
		self.setToolTip('Exercise for <b>exit button</b>.')
		self.setFont(QFont('SansSerif', 13))
		self.resize(600, 450)
		self.move(100, 100)

		button = QPushButton('Exit', self)
		button.resize(button.sizeHint())
		button.move(50, 40)
		button.setToolTip(
			'Click <i>exit</i> button to <b>exit</b> this program')
		button.clicked.connect(QApplication.instance().exit)

		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Main()
	sys.exit(app.exec())
