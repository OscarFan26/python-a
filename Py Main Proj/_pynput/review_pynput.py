from pynput import keyboard, mouse
import sys
import random
import time

m_mouse = mouse.Controller()
m_keyboard = keyboard.Controller()

# # 没有权限，运行不了。
for i in range(20):
    x = random.randint(0, 1400)
    y = random.randint(0, 890)
    m_mouse.position = (x, y)
m_mouse.position = (850, 970)

stat = m_mouse.click(mouse.Button.left)
print(stat)
for i in range(20):
	m_keyboard.type('# -*- 六一儿童节快乐-*- #')
	m_keyboard.press(keyboard.Key.enter)
	m_keyboard.release(keyboard.Key.enter)
	time.sleep(0.5)

sys.exit(0)
