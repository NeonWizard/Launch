import config
import pygame

class Rocket(object):
	def __init__(self, image):
		self.image = pygame.image.load(image)
		self.screenPos = (config.SCREEN_SIZE[0] / 2 - self.image.get_width() / 2, config.SCREEN_SIZE[1] - self.image.get_height())

	def draw(self, surface):
		surface.blit(self.image, self.screenPos)

	def update(self):
		pass
