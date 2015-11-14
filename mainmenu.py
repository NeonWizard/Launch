from __future__ import print_function

import pygame,sys
from pygame.locals import *

class MainMenu(object):
	def __init__(self):
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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

			pygame.display.update()

def main():
	menu = MainMenu()

main()