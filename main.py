import pygame, sys
from pygame.locals import *
sys.dont_write_bytecode = True

import config
from rocket import *

pygame.init()

class Launch:
	def __init__(self):
		# Initiate pygame window stuff
		self.window = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
		pygame.display.set_caption(config.SCREEN_TITLE)

		self.rocket = Rocket("images/rocket.png")

	# Main loop
	def main(self):
		while True:
			self.handleEvents()
			self.update()
			self.draw(self.window)

	# Update everything in game
	def update(self):
		keys = pygame.key.get_pressed()
		self.rocket.update()

	def draw(self, surface):
		# Fill window to clear it
		surface.fill((0, 0, 0))

		# Background
		surface.fill(config.BACKGROUND_COLOR)

		# Object drawing
		self.rocket.draw(self.window)

		pygame.display.update()

	# Handle events
	def handleEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


def main():
	launch = Launch()
	launch.main()

if __name__ == "__main__":
	main()