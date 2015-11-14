from __future__ import print_function

import pygame, sys, random
from pygame.locals import *
import game

import config, button, credits

pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()

def enterGame(menu):
	del menu
	game.main()

def openCredits(menu):
	del menu
	credits.main()

class MainMenu(object):
	def __init__(self, buttons):
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.clock.tick(config.FRAMERATE)

		pygame.mixer.music.play(-1)

		image = pygame.image.load("images/buttons.png")
		buttonimage = image.subsurface((0, 0, image.get_width(), image.get_height() / 2))
		buttonimagehovered = image.subsurface((0, image.get_height() / 2, image.get_width(), image.get_height() / 2))
		buttonfont = pygame.font.Font("freesansbold.ttf", 20)

		self.buttons = []

		for i in range(0, len(buttons)):
			data = buttons[i]
			btn = button.Button(buttonimage, buttonimagehovered, (self.window.get_width() / 2 - buttonimage.get_width() / 2, self.window.get_height() / 2 - buttonimage.get_height() / 2 + (50 * i)))
			btn.set_text(data[0], buttonfont, (0, 0, 0))
			btn.onclick = data[1]
			self.buttons.append(btn)

		titleFont = pygame.font.Font("fonts/redrocket.ttf", 72)
		self.title = titleFont.render("Rocket Ascent", True, (0, 0, 0))

		self.rockets = []
		for i in range(0, 5):
			img = pygame.image.load("images/ship.png")
			scale = 1
			scalex = 100.0*scale/img.get_width()
			scaley = 200.0*scale/img.get_height()
			img = pygame.transform.scale(img, (int(img.get_width()*scalex), int(img.get_height()*scaley)))
			flame = pygame.image.load("images/fire.png")
			flame = pygame.transform.scale(flame, (int(flame.get_width()*scalex), int(flame.get_height()*scaley)))

			surf = pygame.Surface((img.get_width(), img.get_height()+flame.get_height())).convert_alpha()
			surf.fill((0,0,0,0))

			surf.blit(flame, (int(img.get_width() / 2 - flame.get_width() / 2), int(img.get_height() * 0.748)))
			surf.blit(img, (int(surf.get_width() / 2 - img.get_width() / 2), 0))
			data = (surf, [random.randrange(0, self.window.get_width()), random.randrange(0, self.window.get_height())])
			self.rockets.append(data)

	def loop(self):
		while True:
			self.window.fill((200, 200, 200))

			dt = float(self.clock.get_time()) / float(config.FRAMERATE)

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE or event.key == K_RETURN:
						enterGame(self)

				elif event.type == MOUSEBUTTONDOWN:
					for button in self.buttons:
						if button.hovering:
							button.onclick(self)

			for data in self.rockets:
				img, pos = data[0], data[1]
				pos[1] -= 40 * dt
				if (pos[1] + img.get_height()) < 0:
					pos[1] = self.window.get_height() + img.get_height()
				self.window.blit(img, pos)

			for button in self.buttons:
				button.draw(self.window)

			self.window.blit(self.title, (self.window.get_width() / 2 - self.title.get_width() / 2, self.window.get_height() / 4 - self.title.get_height() / 2))

			pygame.display.update()
			self.clock.tick(config.FRAMERATE)

def main():
	pygame.mixer.music.stop()
	pygame.mixer.music.load("music/memento.mp3")
	pygame.mixer.music.set_volume(.4)
	menubuttons = [["Play", enterGame], ["Credits", openCredits], ["Quit", lambda menu: pygame.event.post(pygame.event.Event(QUIT))]]
	menu = MainMenu(menubuttons)
	menu.loop()

if __name__ == "__main__":
	main()
