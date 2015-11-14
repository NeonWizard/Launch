import pygame, sys
from pygame.locals import *

import random

import config
from camera import GameCamera

class PowerUp(object):
	def __init__(self, image, pos):
		self.image = image
		self.pos = pos

	def draw(self, surface):
		surface.blit(self.image, GameCamera.adjust_pos(self.pos))

	def checkCollide(self, rect):
		return rect.collidepoint(GameCamera.adjust_pos(self.pos))
