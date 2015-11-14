import pygame, sys
from pygame.locals import *

import main as mainmenu
from button import *

def enterMenu(credits):
	del credits
	mainmenu.main()

creditsText = """Fuel can icon made by Freepik (http://www.freepik.com) from www.flaticon.com is licensed under Creative Commons BY 3.0.6
http://www.flaticon.com/free-icon/gasoline-gallon_78596

Red Rocket Truetype Font for Windows:
2011 Iconian Fonts - Daniel Zadorozny
http://www.iconian.com/

Background Music:
10,000 - Kick the Habit
"""

class Credits(object):
	def __init__(self):
		self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

		titleFont = pygame.font.Font("fonts/redrocket.ttf", 60)
		self.title = titleFont.render("Credits", True, (0, 0, 0))

		image = pygame.image.load("images/buttons.png")
		buttonimage = image.subsurface((0, 0, image.get_width(), image.get_height() / 2))
		buttonimagehovered = image.subsurface((0, image.get_height() / 2, image.get_width(), image.get_height() / 2))
		buttonfont = pygame.font.Font("freesansbold.ttf", 20)

		self.backButton = Button(buttonimage, buttonimagehovered, (self.window.get_width() / 2 - buttonimage.get_width() / 2, self.window.get_height() * 0.8 - buttonimage.get_height() / 2))
		self.backButton.set_text("Back", buttonfont, (0, 0, 0))
		self.backButton.onclick = enterMenu

		self.creditsText = []
		for line in creditsText.split("\n"):
			if line == "": line = " "
			self.creditsText.append(buttonfont.render(line, True, (0, 0, 0)))

	def main(self):
		while True:
			self.window.fill((200, 200, 200))

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == MOUSEBUTTONDOWN:
					if self.backButton.hovering:
						self.backButton.onclick(self)

			self.window.blit(self.title, (self.window.get_width() / 2 - self.title.get_width() / 2, self.window.get_height() / 4 - self.title.get_height() / 2))
			self.backButton.draw(self.window)
			runningheight = 0
			for line in self.creditsText:
				self.window.blit(line, (self.window.get_width() / 2 - line.get_width() / 2, self.window.get_height() / 3 - line.get_height() / 2 + runningheight))
				runningheight += line.get_height()

			pygame.display.update()

def main():
	credits = Credits()
	credits.main()
