import config
import pygame

class Rocket:
	def __init__(self, image):
		self.image = pygame.image.load(image)
		self.screenPosX = config.SCREEN_WIDTH / 2 - self.image.get_width() / 2
		self.screenPosY = config.SCREEN_HEIGHT-self.image.get_height()
		self.dx = 0
		self.dy = 0
		self.moving = False

	def draw(self, surface):
		surface.blit(self.image, (self.screenPosX, self.screenPosY))

	def update(self, key):
		if self.moving and key == 'w':
			if self.dy > -50:
				self.dy -= 1
			self.screenPosY += self.dy