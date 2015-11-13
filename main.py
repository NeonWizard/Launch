import pygame, sys
from pygame.locals import *

import config
from peripherals import *
from rocket import *

pygame.init()

MOUSE = MouseInfo((0,0))
KEYS = KeyInfo()

class Launch:
	def __init__(self):
		self.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
		self.rocket = Rocket("images/rocket.png")

	def main(self):
		while True:
			self.window.fill(config.SPILL_COLOR)
			self.window.blit(config.SPILL_IMAGE, (0, 0))
			pygame.display.set_caption(config.SCREEN_TITLE)

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == MOUSEMOTION:
					MOUSE.updatePos(event.pos)

				elif event.type == KEYDOWN:
					KEYS.handle(event.key)

			pygame.display.update()


def main():
	launch = Launch()
	launch.main()


if __name__ == "__main__":
	main()