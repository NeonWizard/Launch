from __future__ import print_function

import pygame, sys, random
from pygame.locals import *
import main as maingame

import config, button

pygame.init()

class MainMenu(object):
	def __init__(self, buttons):
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.mousePos = (0,0)
		config.SCREEN_SIZE = self.window.get_size()

		image = pygame.image.load("images/buttons.png")
		buttonimage = image.subsurface((0, 0, image.get_width(), image.get_height() / 2))
		buttonimagehovered = image.subsurface((0, image.get_height() / 2, image.get_width(), image.get_height() / 2))
		buttonfont = pygame.font.Font("freesansbold.ttf", 20)
		
		self.buttons = []

		for i in range(0, len(buttons)):
			data = buttons[i]
			btn = button.Button(buttonimage, buttonimagehovered, (config.SCREEN_SIZE[0] / 2 - buttonimage.get_width() / 2, config.SCREEN_SIZE[1] / 2 - buttonimage.get_height() / 2 + (50 * i)))
			btn.set_text(data[0], buttonfont, (0, 0, 0))
			btn.onclick = data[1]
			self.buttons.append(btn)

		self.titleFont = pygame.font.Font("freesansbold.ttf", 32)
		self.titleMsg = self.titleFont.render("Rocket Ascent", True, (0, 0, 0))

		self.rockets = []
		for i in range(0, 20):
			data = (pygame.transform.scale(pygame.image.load("dev/patesship.png"), (20, 40)), [random.randrange(0, self.window.get_width()), random.randrange(0, self.window.get_height())])
			self.rockets.append(data)

	def loop(self):
		while True:
			self.window.fill((200,200,200))

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.event.post(pygame.event.Event(QUIT))

				elif event.type == MOUSEMOTION:
					for button in self.buttons:
						button.checkHover(event.pos)

				elif event.type == MOUSEBUTTONDOWN:
					for button in self.buttons:
						if button.hovering:
							button.onclick()

			for data in self.rockets:
				img, pos = data[0], data[1]
				pos[1] -= 5
				if (pos[1] + img.get_height()) < 0:
					pos[1] = self.window.get_height() + img.get_height()
				self.window.blit(img, pos)

			for button in self.buttons:
				button.draw(self.window)

			self.window.blit(self.titleMsg, (config.SCREEN_SIZE[0] / 2 - self.titleMsg.get_width() / 2, config.SCREEN_SIZE[1] / 4 - self.titleMsg.get_height() / 2))

			pygame.display.update()

def main():
	menubuttons = [["Play", maingame.main], ["Quit", lambda x=None: pygame.event.post(pygame.event.Event(QUIT))], ["Print Hello", lambda x=None: print("Hello")]]
	menu = MainMenu(menubuttons)
	menu.loop()

if __name__ == "__main__":
	main()
