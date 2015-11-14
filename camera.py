import pygame

import config
import terraingen

# All things visually relative
class Camera(object):
	def __init__(self):
		self.pos = (0, 0)

		self.chunk = [0, 0]

		self.groundChunk = None

	def set_pos(self, pos, y=None):
		if not (y is None):
			pos = (pos, y)
		self.pos = pos
		self.chunk = [round(float(self.pos[0])/config.SCREEN_SIZE[0]), round(float(self.pos[1])/config.SCREEN_SIZE[1])]

	def adjust_pos(self, pos, y=None):
		if (not y is None):
			pos = [pos, y]
		return (self.pos[0] + pos[0], self.pos[1] + pos[1])

	def displayChunks(self, surface):
		if not self.groundChunk:
			self.groundChunk = terraingen.generateHills(config.SCREEN_SIZE, 10)

		if self.chunk[1] == 0:
			for i in range(-1, 2):
				surface.blit(self.groundChunk, self.adjust_pos(surface.get_width()*(i-self.chunk[0]), 0))
		#surface.blit()

GameCamera = Camera()
