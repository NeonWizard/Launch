from __future__ import print_function

import pygame

class Button(object):
	def __init__(self, rect, color):
		self.rect = rect
		self.color = color

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

	# override me
	def onclick(self):
		print("clicked button ", self)
