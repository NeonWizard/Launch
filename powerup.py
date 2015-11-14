import pygame, sys
from pygame.locals import *


class PowerUp:
	def __init__(self, window):
		self.window = window

	def draw(self):
		self.window.blit(pygame.image.load("images/fuel.png"), (0,0))