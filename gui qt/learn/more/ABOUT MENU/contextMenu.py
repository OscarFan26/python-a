# encoding: utf-8 #
"""
==========
File Name:              contextMenu
Author:                 Oscar Fan
Date:                   2022/1/29
requirements:           PyQt6
==========
"""
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QMenu


class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 100, 800, 400)
		self.setWindowTitle('Test')
		self.show()

	def contextMenuEvent(self, event):
		cmenu = QMenu(self)
		newAct = cmenu.addAction('New')
		openAct = cmenu.addAction('Open')
		quitAct = cmenu.addAction('Quit')

		# 必须要让右键点击后的menu菜单能够一直存在(直到用户再次点击)
		# 我们就必须要使用menu.exec_的方法让它一直存在
		# 但是只是用这个方法的话,出现的menu菜单不是在我们的主窗口上面\
		# 而是在我们的主窗口外面(而且是0, 0的位置),意思就是menu要运行,\
		# 但是它不知道我们主窗口运行在哪个位置,
		# 所以我们要用mapToGlobal(event.pos())这个函数,将主函数里面的\
		# 主窗口永真循环的exec_函数和这个联系起来,\
		# 这时我们获得的是事件触发(右键点击在哪里)时候的位置坐标\
		# event.pos,mapToGlobal返回的是一个位置坐标,
		# 同时让menu运行在这个位置,而不是默认的(0, 0)
		action = cmenu.exec(self.mapToGlobal(event.pos()))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	m = Main()
	sys.exit(app.exec())

