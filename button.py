from __future__ import print_function

import pygame, config

class Button(object):
	def __init__(self, image, window, pos):
		self.image = image
		self.window = window
		self.buttonPos = pos
		self.hovering = False

	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

	# override me
	def onclick(self):
		print("clicked button ", self)

	def update(self):
		if self.hovering:
			self.window.blit(self.image, self.buttonPos, (0, self.image.get_height() / 2, self.image.get_width(), self.image.get_height() / 2))
		else:	
			self.window.blit(self.image, self.buttonPos, (0, 0, self.image.get_width(), self.image.get_height() / 2))

	def checkHover(self, mousePos):
		self.buttonRect = pygame.Rect(self.buttonPos[0], self.buttonPos[1], self.image.get_width(), self.image.get_height() / 2)
		if self.buttonRect.collidepoint(mousePos):
			self.hovering = True
		else:
			self.hovering = False
