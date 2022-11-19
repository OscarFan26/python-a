# encoding: utf-8 #
"""
==========
File Name:              4 popup                    
Author:                 Oscar Fan
Date:                   2022/1/18
requirements:   PyQt6
==========
"""
import sys

from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt6.QtGui import QFont


class Main(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setWindowTitle('4 Popup')
		self.setGeometry(300, 300, 350, 200)
		self.setToolTip("A window for exersice '4 popup'")
		self.setFont(QFont('SansSerif', 12))
		self.show()

	def closeEvent(self, event):
		"""
		QMessageBox.question(self, "title", "information", button1 | button2 | ... | button n
		)
		button will be in QMessageBox.StandardButtons.?
		"""
		reply = QMessageBox.question(self, "EXIT QUESTION   ",
		                             "Are you sure to exit?\t\t\t\n\n\n",
		                             QMessageBox.StandardButtons.Yes | QMessageBox.StandardButtons.No)
		if reply == QMessageBox.StandardButtons.Yes:  # 判断点击的按钮类型
			event.accept()  # 点是的判断
		else:
			event.ignore()  # 点否的判断


if __name__ == '__main__':
	app = QApplication(sys.argv)
	m = Main()
	sys.exit(app.exec())
