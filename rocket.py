import config
import pygame
import math
from pygame.locals import *

def rot_center(image, angle):
	"""rotate an image while keeping its center and size"""
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

TRANSPARENCY = pygame.Color(0, 0, 0, 0)

class Rocket(object):
	def __init__(self, image):
		image = pygame.image.load(image)
		pblll = ((image.get_height() / 2) ** 2 + (image.get_width() / 2) ** 2) ** .5
		t = pblll * 2
		self.baseImage = pygame.Surface((t, t)).convert_alpha()
		self.baseImage.fill(TRANSPARENCY)
		self.baseImage.blit(image, ((t-image.get_width())/2, (t-image.get_height())/2))
		self.image = self.baseImage.copy()
		self.size = (self.image.get_width(), self.image.get_height())

		self.maxSpeed = 10
		self.velocity = 0
		self.rotation = 0
		self.screenPos = [config.SCREEN_SIZE[0] / 2 - self.image.get_width() / 2, config.SCREEN_SIZE[1] - self.image.get_height()]

	def draw(self, surface):
		surface.blit(self.image, self.screenPos)

	def update(self, dt, keys):
		if self.screenPos[1] < config.SCREEN_SIZE[1] - self.size[1]:
			self.velocity -= 3 * dt
		else:
			self.screenPos[1] = config.SCREEN_SIZE[1] - self.size[1]

		if keys[K_UP]:
			self.velocity += 6 * dt
			self.velocity = min(self.maxSpeed, self.velocity)

		if keys[K_LEFT]:
			self.rotation -= 6 * dt
		elif keys[K_RIGHT]:
			self.rotation += 6 * dt

		self.image = rot_center(self.baseImage, -self.rotation)

		self.move(dt)

	def move(self, dt):
		self.screenPos[0] += math.sin(math.radians(self.rotation)) * self.velocity
		self.screenPos[1] = min(config.SCREEN_SIZE[1]-self.size[1], self.screenPos[1] - (math.cos(math.radians(self.rotation)) * self.velocity))