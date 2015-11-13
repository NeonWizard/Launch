import config
import pygame

class Rocket:
	def __init__(self, image):
		self.image = pygame.image.load(image)
		self.screenPosX = config.SCREEN_WIDTH / 2 - self.image.get_width() / 2
		self.screenPosY =  config.SCREEN_HEIGHT - 400

	def draw(self, surface):
		surface.blit(self.image, (self.screenPosX, self.screenPosY))

	def update(self, keys):
		if keys[]