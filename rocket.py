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

def addVectors(vectorOne, vectorTwo):
	x = (math.sin(vectorOne[0]) * vectorOne[1]) + (math.sin(vectorTwo[0]) * vectorTwo[1])
	y = (math.cos(vectorOne[0]) * vectorOne[1]) + (math.cos(vectorTwo[0]) * vectorTwo[1])
	length = math.hypot(x, y)
	angle = 0.5 * math.pi - math.atan2(y, x)
	return (angle, length)

class Rocket(object):
	def __init__(self, image):
		image = pygame.transform.scale(pygame.image.load(image), (100, 200))
		pblll = ((image.get_height() / 2) ** 2 + (image.get_width() / 2) ** 2) ** .5
		t = pblll * 2
		self.baseImage = pygame.Surface((t, t)).convert_alpha()
		self.baseImage.fill(TRANSPARENCY)
		self.baseImage.blit(image, ((t-image.get_width())/2, (t-image.get_height())/2))
		self.image = self.baseImage.copy()
		self.size = (self.image.get_width(), self.image.get_height())

		self.maxSpeed = 10
		self.velocity = 0
		self.direction = 0
		self.pos = [config.SCREEN_SIZE[0] / 2 - self.image.get_width() / 2, 0]

		self.fuel = 1000

	def draw(self, surface):
		if self.pos[1] < config.SCREEN_SIZE[1]/2-self.size[1]/2:
			surface.blit(self.image, (config.SCREEN_SIZE[0]/2-self.size[0]/2, max(config.SCREEN_SIZE[1]/2-self.size[1]/2, config.SCREEN_SIZE[1]-self.size[1]-self.pos[1])))
		else:
			surface.blit(self.image, (config.SCREEN_SIZE[0]/2-self.size[0]/2, config.SCREEN_SIZE[1]/2-self.size[1]/2))

	def update(self, dt, keys):
		# Apply gravity
		if self.pos[1] > 0:
			self.direction, self.velocity = addVectors((self.direction, self.velocity), (config.GRAVITY[0], config.GRAVITY[1]*dt))
		else:
			self.velocity = 0

		if self.fuel > 0:
			if keys[K_UP]:
				self.fuel -= 5 * dt
				self.velocity += 6 * dt
				self.velocity = min(self.maxSpeed, self.velocity)

			if keys[K_LEFT]:
				self.fuel -= dt
				self.direction -= .5 * dt
			elif keys[K_RIGHT]:
				self.fuel -= dt
				self.direction += .5 * dt

		self.image = rot_center(self.baseImage, -math.degrees(self.direction))

		self.move()

	def move(self):
		self.pos[0] += math.sin(self.direction) * self.velocity
		self.pos[1] += math.cos(self.direction) * self.velocity

		# Preventing movement below starting point
		self.pos[1] = max(0, self.pos[1])
