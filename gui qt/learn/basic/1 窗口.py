# encoding: utf-8 #
"""
==========
File Name:              1 窗口                    
Author:                 Oscar Fan
Date:                   2022/1/9
                        
==========
requirements:  pyqt6==6.0.3
"""
import sys

from PyQt6.QtWidgets import QApplication, QWidget


def main():
	app = QApplication(sys.argv)  # 创建一个app

	w = QWidget()  # 别说，写就对了

	w.resize(600, 400)  # 定义窗口大小
	w.move(100, 50)  # 把窗口移动到 x 100 y 50 的位置
	w.setWindowTitle('Qt Window')  # 设置标题(窗口名称)

	w.show()  # 显示窗口
	sys.exit(app.exec())  # 直到退出才杀进程(这样可以杀掉所有子QWidget)


if __name__ == '__main__':
	main()  # 运行该程序
