# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/5/15 14:32
# Project name: pygame_proj
# IDE: PyCharm
# File name: l1--.py
import pygame
from pygame.locals import *
import sys

pygame.init()
ima = pygame.image.load('py_logo.jpg')
window = pygame.display.set_mode((850, 650))
pygame.display.set_caption('My window')
pygame.display.set_icon(ima)
window.fill('pink')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit(True)
		if event.type == KEYUP:
			if event.key == K_UP:
				pass
			if event.key == K_DOWN:
				pass
			if event.key == K_LEFT:
				pass
			if event.key == K_RIGHT:
				pass
			if event.key == K_j:
				pass

			if event.key == K_r:
				pass
			if event.key == K_SPACE:
				pass
			if event.key == K_ESCAPE:
				print('you gonna exit.')
				sys.exit()
			if event.key == K_h:
				print('help_me!')
			if event.key == K_1:
				print('stupid don\'t touch it.')
	pygame.display.update()
