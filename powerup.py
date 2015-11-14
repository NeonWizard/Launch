import pygame, sys
from pygame.locals import *

import random

import config
from camera import GameCamera

class PowerUp(object):
	def __init__(self, image, pos):
		self.image = image
		self.pos = pos
		self.noadjust = False

	def draw(self, surface):
		surface.blit(self.image, self.pos if self.noadjust else GameCamera.adjust_pos(self.pos))

	def checkCollide(self, rect):
		return rect.collidepoint(self.pos if self.noadjust else GameCamera.adjust_pos(self.pos))
