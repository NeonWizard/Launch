from __future__ import print_function

# standard library modules
import sys, math, random
sys.dont_write_bytecode = True

# third party modules
import pygame
from pygame.locals import *

# our modules
import config
from rocket import *
from camera import GameCamera
import terraingen
import main as mainmenu
import powerup

# Initiate pygame things
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()

FPSFONT = pygame.font.Font(None, 48)

WHITE = pygame.Color(255, 255, 255)

sound = pygame.mixer.Sound("sound/engine.wav")

def enterMenu(game):
	del game
	mainmenu.main()

class Launch():
	def __init__(self):
		# Initiate pygame window stuff
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		pygame.display.set_caption(config.SCREEN_TITLE)
		config.SCREEN_SIZE = self.window.get_size()

		self.clock = pygame.time.Clock()
		self.clock.tick(config.FRAMERATE)

		self.rocket = Rocket("images/ship.png")

		self.initPowerUp()

		self.layers = [0 for _ in range(0, 1000)]

		#pygame.mixer.music.play(-1)

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
					enterMenu(self)

				elif event.key == K_r:
					self.rocket.__init__("images/ship.png")

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

		rocketRect = pygame.Rect(self.rocket.drawpos[0], self.rocket.drawpos[1], self.rocket.image.get_width(), self.rocket.image.get_height())
		for fuelCan in self.fuelCans:
			if fuelCan.checkCollide(rocketRect):
				self.fuelCans.remove(fuelCan)
				self.rocket.fuel += 100

		self.clock.tick(config.FRAMERATE)

	def drawbackground(self, surface):
		surface.fill((155, 255, 255))

		horizontalOffset = int(round(float(GameCamera.pos[0]) / self.window.get_width()))
		layer = int(round(float(GameCamera.pos[1]) / self.window.get_height()))

		self.layer = layer

		for i in range(-1, 2):
			for i2 in range(-1, 2):
				if layer == 0 and i2 != 0: continue
				if self.layers[layer-i2] == 0:
					self.layers[layer-i2] = terraingen.generateLayer(layer-i2, config.SCREEN_SIZE, 10)
				layersurf = self.layers[layer-i2]
				surface.blit(layersurf, GameCamera.adjust_pos(surface.get_width() * (i - horizontalOffset), -(self.window.get_height() * layer) + self.window.get_height() * i2))

	def initPowerUp(self):
		fuelCanImage = pygame.image.load("images/fuel.png")
		fuelCanImage = pygame.transform.scale(fuelCanImage, (int(fuelCanImage.get_width() / 8), int(fuelCanImage.get_height() / 8)))

		self.fuelCans = []
		for i in range(0, 5):
			self.fuelCans.append(powerup.PowerUp(fuelCanImage, [random.randrange(0, config.SCREEN_SIZE[0] - fuelCanImage.get_width()), random.randrange(0, config.SCREEN_SIZE[1] - fuelCanImage.get_height())]))

	def draw(self, surface):
		# Background
		self.drawbackground(surface)

		# Status messages
		surface.blit(FPSFONT.render(str(self.clock.get_fps()), True, WHITE), (0, 0))
		surface.blit(FPSFONT.render("FUEL: " + str(int(round(self.rocket.fuelPercent, 2) * 100)) + "%", True, WHITE), (0, 50))
		surface.blit(FPSFONT.render("Height: " + str(int(self.rocket.pos[1])), True, WHITE), (0, 100))
		surface.blit(FPSFONT.render("Layer: " + str(int(self.layer)), True, WHITE), (0, 150))

		# Draw our objects
		self.rocket.draw(self.window)

		for fuelCan in self.fuelCans:
			fuelCan.draw(self.window)

		pygame.display.update()

def main():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music/10000.mp3")
	pygame.mixer.music.set_volume(.2)
	launch = Launch()
	launch.main()
