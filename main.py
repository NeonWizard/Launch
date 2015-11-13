import pygame, sys
from pygame.locals import *

import config

pygame.init()

class Launch:
	def __init__(self):
		self.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

	def main(self):
		while True:
			self.window.fill(config.SPILL_COLOR)
			self.window.blit(config.SPILL_IMAGE, (0, 0))
			pygame.display.set_caption(config.SCREEN_TITLE)

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()



def main():
	launch = Launch()
	launch.main()


if __name__ == "__main__":
	main()