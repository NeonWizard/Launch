from __future__ import print_function

# standard library modules
import sys
sys.dont_write_bytecode = True

# third party modules
import pygame
from pygame.locals import *
sys.dont_write_bytecode = True

# our modules
import config
from rocket import *
from mainmenu import *

pygame.init()

class Launch():
	def __init__(self):
		# Initiate pygame window stuff
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		pygame.display.set_caption(config.SCREEN_TITLE)
		config.SCREEN_SIZE = self.window.get_size()

		self.rocket = Rocket("images/rocket.png")
		self.mainmenu = MainMenu()

	# Main loop
	def main(self):
		while True:
			self.handleEvents()
			self.update()
			self.draw(self.window)

	def handleEvents(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.event.post(pygame.event.Event(QUIT))

	# Update everything in game
	def update(self):
		keys = pygame.key.get_pressed()
		self.rocket.update()

	def draw(self, surface):
		# Fill window to clear it
		surface.fill((0, 0, 0))

		# Background
		surface.fill(config.BACKGROUND_COLOR)

		# Draw our objects
		self.rocket.draw(self.window)

		pygame.display.update()

def main():
	launch = Launch()
	launch.main()

main()