import config
import pygame
import math
from pygame.locals import *
from camera import GameCamera

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
		scale = 0.33
		image = pygame.image.load(image)
		image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))

		diag = math.sqrt((image.get_height() / 2) ** 2 + (image.get_width() / 2) ** 2) * 2

		self.baseImage = pygame.Surface((diag, diag)).convert_alpha()
		self.baseImage.fill(TRANSPARENCY)

		self.flameImage = pygame.image.load("images/fire.png")
		self.flameImage = pygame.transform.scale(self.flameImage, (int(self.flameImage.get_width() * scale), int(self.flameImage.get_height() * scale)))

		self.image = self.baseImage.copy()

		self.image.blit(self.flameImage, (int(self.baseImage.get_width() / 2 - self.flameImage.get_width() / 2), int(image.get_height() * 0.748)))
		self.image.blit(image, ((diag - image.get_width()) / 2, (diag - image.get_height()) / 2))

		self.flameImage = self.image.copy()
		self.flamelessImage = self.baseImage.copy()
		self.flamelessImage.blit(image, ((diag - image.get_width()) / 2, (diag - image.get_height()) / 2))

		self.maxSpeed = 5
		self.velocity = 0
		self.direction = 0
		self.drawpos = [0, 0]
		self.pos = [0, config.SCREEN_SIZE[1]*21]

		self.fuel = 1000
		self.fullFuel = self.fuel
		self.fuelPercent = 1

	def draw(self, surface):
		if self.pos[1] < config.SCREEN_SIZE[1]/2-self.image.get_height()/2:
			self.drawpos = (config.SCREEN_SIZE[0]/2-self.image.get_width()/2, max(config.SCREEN_SIZE[1]/2-self.image.get_height()/2, config.SCREEN_SIZE[1]-self.image.get_height()-self.pos[1]))
		else:
			self.drawpos = (config.SCREEN_SIZE[0]/2-self.image.get_width()/2, config.SCREEN_SIZE[1]/2-self.image.get_height()/2)
		surface.blit(self.image, self.drawpos)

		try:
			pygame.draw.rect(surface, (255 - int(255 * self.fuelPercent), int(255 * self.fuelPercent), 0), (config.SCREEN_SIZE[0] - 225, config.SCREEN_SIZE[1] - 50, 200 * self.fuelPercent, 25))
		except:
			pass
		surface.blit(pygame.image.load("images/fuelBar.png"), (config.SCREEN_SIZE[0] - 225, config.SCREEN_SIZE[1] - 50))

	def update(self, dt, keys):
		# Apply gravity
		if self.pos[1] > 0:
			self.direction, self.velocity = addVectors((self.direction, self.velocity), (config.GRAVITY[0], config.GRAVITY[1]*dt))
		else:
			self.velocity = 0

		gotInput = False
		if self.fuel > 0:
			if keys[K_UP]:
				self.fuel -= 5 * dt
				self.velocity += 3 * dt
				self.velocity = min(self.maxSpeed, self.velocity)
				gotInput = True

			if keys[K_LEFT]:
				self.fuel -= dt
				self.direction -= .5 * dt
				gotInput = True
			elif keys[K_RIGHT]:
				self.fuel -= dt
				self.direction += .5 * dt
				gotInput = True
			self.fuelPercent = float(self.fuel / self.fullFuel)

		if gotInput:
			self.image = rot_center(self.flameImage, -math.degrees(self.direction))
		else:
			self.image = rot_center(self.flamelessImage, -math.degrees(self.direction))

		self.move()

	def move(self):
		self.pos[0] += math.sin(self.direction) * self.velocity
		self.pos[1] += math.cos(self.direction) * self.velocity

		GameCamera.set_pos((-self.pos[0], self.pos[1]))

		# Preventing movement below starting point
		self.pos[1] = max(0, self.pos[1])
