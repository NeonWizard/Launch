import pygame, sys
from pygame.locals import *

import random

import config
from camera import GameCamera

class PowerUp:
	def __init__(self, window, image):
		self.window = window
		self.image = image
		config.SCREEN_SIZE = self.window.get_size()
		self.positionList = self.getPos()

	def draw(self):
		for pos in self.positionList:
			self.window.blit(pygame.transform.scale(self.image, (int(self.image.get_width() / 8), int(self.image.get_height() / 8))), GameCamera.adjust_pos(pos))

	def getPos(self):
		self.positions = []
		for i in range(0,5):
			self.positions.append([random.randrange(0, config.SCREEN_SIZE[0] - self.image.get_width()), random.randrange(0, config.SCREEN_SIZE[1] - self.image.get_height())])
		return self.positions