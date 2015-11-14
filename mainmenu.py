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
		self.playButton = button.Button(self.image, self.window, (config.SCREEN_SIZE[0] / 2 - self.image.get_width() / 2, config.SCREEN_SIZE[1] / 2 - self.image.get_height() / 2 / 2 - 25))
		self.quitButton = button.Button(self.image, self.window, (config.SCREEN_SIZE[0] / 2 - self.image.get_width() / 2, config.SCREEN_SIZE[1] / 2 - self.image.get_height() / 2 / 2 + 25))
		self.defaultFont = pygame.font.Font("freesansbold.ttf", 20)
		self.playMsg = self.defaultFont.render("Play", True, (255, 0, 0))
		self.quitMsg = self.defaultFont.render("Quit", True, (255, 0, 0))
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
					self.playButton.checkHover(self.mousePos)
					self.playButton.update()
					self.quitButton.checkHover(self.mousePos)
					self.quitButton.update()

				elif event.type == MOUSEBUTTONDOWN:
					if self.playButton.hovering:
						from main import *
						pygame.quit()
						sys.exit()

					elif self.quitButton.hovering:
						pygame.quit()
						sys.exit()

					else:
						print "Not Clicked!"

			self.window.blit(self.playMsg, (config.SCREEN_SIZE[0] / 2 - self.playMsg.get_width() / 2, config.SCREEN_SIZE[1] / 2 - self.playMsg.get_height() / 2 - 25))
			self.window.blit(self.quitMsg, (config.SCREEN_SIZE[0] / 2 - self.playMsg.get_width() / 2, config.SCREEN_SIZE[1] / 2 - self.playMsg.get_height() / 2 + 25))

			pygame.display.update()

def main():
	menu = MainMenu()

main()