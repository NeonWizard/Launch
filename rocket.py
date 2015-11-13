import config
import pygame
from pygame.locals import *

class Rocket(object):
	def __init__(self, image):
		self.image = pygame.image.load(image)
		self.screenPos = (config.SCREEN_SIZE[0] / 2 - self.image.get_width() / 2, config.SCREEN_SIZE[1] - self.image.get_height())
		self.size = (self.image.get_width(), self.image.get_height())

		self.maxSpeed = 10
		self.velocity = [0, 0]
		self.rotation = 0

	def draw(self, surface):
		surface.blit(self.image, self.screenPos)

	def update(self, dt, keys):
		if self.screenPos[1] < config.SCREEN_SIZE[1]-self.size[1]:
			self.velocity[1] -= 3 * dt
		else:
			self.velocity[1] = 0

		if keys[K_UP]:
			self.velocity[1] += 6 * dt
			self.velocity[1] = min(self.maxSpeed, self.velocity[1])

		self.move(dt)

	def move(self, dt):
		self.screenPos = (self.screenPos[0] + self.velocity[0],  min(config.SCREEN_SIZE[1]-self.size[1], self.screenPos[1] - self.velocity[1]))