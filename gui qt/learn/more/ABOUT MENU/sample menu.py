# encoding: utf-8 #
"""
==========
File Name:              sample menu                    
Author:                 Oscar Fan
Date:                   2022/1/18
requirements:           PyQt6
==========
"""
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		"""
		QAction是行为抽象类，包括菜单栏，工具栏，或自定义键盘快捷方式。
		在上面的三行中，创建了一个带有特定图标和
		'Exit'
		标签的行为。
		此外，第二行还为该行为定义了一个快捷方式。
		第三行创建一个状态提示，当我们将鼠标指针悬停在菜单项上时，状态栏中就会显示这个提示。
		"""
		exitAct = QAction(QIcon('../src/exit.png'), '&Exit', self)
		exitAct.setShortcut('Esc')
		exitAct.setStatusTip('Exit Application')
		# 当选择指定的行为时，触发了一个信号，
		# 这个信号连接了 QApplication 组件的退出操作，这会终止这个应用程序。
		exitAct.triggered.connect(QApplication.instance().quit)

		self.statusBar()
		menubar = self.menuBar()
		fileMenu = menubar.addMenu("&File")
		fileMenu.addAction(exitAct)
		# menuBar 方法创建了一个菜单栏，然后使用 addMenu 创建一个文件菜单，使用 addAction 创建一个行为。
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Simple menu')
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	m = Main()
	sys.exit(app.exec())
