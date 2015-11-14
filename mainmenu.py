import pygame,sys
from pygame.locals import *

import config, button

pygame.init()

class MainMenu(object):
	def __init__(self):
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.mousePos = (0,0)
		config.SCREEN_SIZE = self.window.get_size()
		self.image = pygame.image.load("images/buttons.png")
		self.button = button.Button(self.image, self.window, (config.SCREEN_SIZE[0] / 2 - self.image.get_width() / 2, config.SCREEN_SIZE[1] / 2 - self.image.get_height() / 2 / 2))
		self.defaultFont = pygame.font.Font("freesansbold.ttf", 20)
		self.playMsg = self.defaultFont.render("Play", True, (255, 0, 0))
		self.loop()

	def loop(self):
		self.window.fill((200,200,200))
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()

				elif event.type == MOUSEMOTION:
					self.mousePos = pygame.mouse.get_pos()
					self.button.checkHover(self.mousePos)
					self.button.update()

				elif event.type == MOUSEBUTTONDOWN:
					if self.button.hovering:
						from main import *
						pygame.quit()
						sys.exit()
					else:
						print "Not Clicked!"

			self.window.blit(self.playMsg, (config.SCREEN_SIZE[0] / 2 - self.playMsg.get_width() / 2, config.SCREEN_SIZE[1] / 2 - self.playMsg.get_height() / 2))

			pygame.display.update()

def main():
	menu = MainMenu()

main()