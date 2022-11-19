import time
import random
import sys
from pynput import mouse, keyboard

m_mouse = mouse.Controller()  # 创建一个鼠标的实例
m_board = keyboard.Controller()  # 创建一个键盘的实例
time.sleep(3)

# 10-14没有权限，运行不了
# for i in range(20):
#     x = random.randint(0, 1400)
#     y = random.randint(0, 890)
#     m_mouse.position = (x, y) #移动到指定的坐标
#     print(i)
m_mouse.position = (850, 970)

m_mouse.click(mouse.Button.left)  # 点击鼠标左键,右键是right
for i in range(20):
	m_board.type('#-*-   六一儿童节快乐!   -*- #')  # 控制键盘打字
	m_board.press(keyboard.Key.backspace)  # 按下enter键
	m_board.release(keyboard.Key.backspace)
	time.sleep(0.5)

sys.exit(0)
