from __future__ import print_function

import pygame

class Button(object):
	def __init__(self, x, y, w, h, color):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = color

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

	# override me
	def onclick(self):
		print("clicked button ", self)
