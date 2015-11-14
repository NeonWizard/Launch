import pygame

import config

# All things visually relative
class Camera(object):
	def __init__(self):
		self.pos = (0, 0)

		self.chunk = [0, 0]

	def set_pos(self, pos, y=None):
		if not (y is None):
			pos = (pos, y)
		self.pos = pos
		self.chunk = [round(float(self.pos[0])/config.SCREEN_SIZE[0]), round(float(self.pos[1])/config.SCREEN_SIZE[1])]

	def adjust_pos(self, pos, y=None):
		if (not y is None):
			pos = [pos, y]
		return (self.pos[0] + pos[0], self.pos[1] + pos[1])

	def loadChunks(self, surface):
		pass

GameCamera = Camera()
