from __future__ import print_function

# standard library modules
import sys
sys.dont_write_bytecode = True

# third party modules
import pygame
from pygame.locals import *

# our modules
import config
from rocket import *
from camera import GameCamera

# Initiate pygame things
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()

FPSFONT = pygame.font.Font(None, 48)

WHITE = pygame.Color(255, 255, 255)

sound = pygame.mixer.Sound("sound/engine.wav")

class Launch():
	def __init__(self):
		# Initiate pygame window stuff
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		pygame.display.set_caption(config.SCREEN_TITLE)
		config.SCREEN_SIZE = self.window.get_size()

		self.clock = pygame.time.Clock()
		self.clock.tick(config.FRAMERATE)

		self.rocket = Rocket("images/ship.png")
		self.backgroundImage = pygame.transform.scale(pygame.image.load("images/ground.png"), self.window.get_size())

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

				elif event.key == K_r:
					self.rocket.__init__("dev/patesship.png")

				elif event.key == K_UP:
					if not pygame.mixer.get_busy():
						#sound.play(-1)
						pass

			elif event.type == KEYUP:
				if event.key == K_UP:
					#sound.stop()
					pass

	# Update everything in game
	def update(self):
		dt = float(self.clock.get_time()) / float(config.FRAMERATE)
		keys = pygame.key.get_pressed()

		self.rocket.update(dt, keys)

		self.clock.tick(config.FRAMERATE)

	def draw(self, surface):
		# Fill window to clear it
		surface.fill((0, 0, 0))

		# Background
		surface.fill(config.BACKGROUND_COLOR)

		surface.blit(self.backgroundImage, GameCamera.adjust_pos((0, 0)))

		# Framerate
		surface.blit(FPSFONT.render(str(self.clock.get_fps()), True, WHITE), (0, 0))
		surface.blit(FPSFONT.render("FUEL: " + str(int(self.rocket.fuel)), True, WHITE), (0, 50))
		surface.blit(FPSFONT.render("Height: " + str(int(self.rocket.pos[1])), True, WHITE), (0, 100))

		# Draw our objects
		self.rocket.draw(self.window)

		pygame.display.update()

def main():
	launch = Launch()
	launch.main()

main()
