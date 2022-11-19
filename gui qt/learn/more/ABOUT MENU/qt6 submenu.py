import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu
from PyQt6.QtGui import QAction


class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		menubar = self.menuBar()
		filemenu = menubar.addMenu('File')
		impMenu = QMenu('Import', self)

		impAct = QAction('>>> Import Anything you want <<<', self)
		impMenu.addAction(impAct)

		newAct = QAction('New', self)
		# 在文件中添加newAct和impMenu
		filemenu.addAction(newAct)
		filemenu.addMenu(impMenu)

		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('A Window for Submenu')
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	m = Main()
	sys.exit(app.exec())
