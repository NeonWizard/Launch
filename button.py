from __future__ import print_function

import pygame, config

class Button(object):
	def __init__(self, rectorimage, colororhoverimage, hovercolororpos):
		if type(rectorimage) == pygame.Surface:
			self.isImage = True
			self.image = rectorimage
			self.hoverimage = colororhoverimage
			self.pos = hovercolororpos
			self.rect = pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height())
		else:
			self.isImage = False
			self.rect = rectorimage
			self.color = colororhoverimage
			self.hovercolor = hovercolororpos
		self.hovering = False
		self.text = False

	def set_text(self, text, font, textcolor):
		if text == "":
			self.text == False
		self.text = font.render(text, True, textcolor)

	def draw(self, surface):
		if self.isImage:
			surface.blit(self.hoverimage if self.hovering else self.image, self.pos)
			if self.text:
				surface.blit(self.text, (self.rect.x + self.rect.w / 2 - (self.text.get_width() / 2), self.rect.y + self.rect.h / 2 - (self.text.get_height() / 2)))
		else:
			pygame.draw.rect(surface, self.hoveredcolor if self.hovering else self.color, self.rect)
			if self.text:
				surface.blit(self.text, (self.rect.x + self.rect.w / 2 - (self.text.get_width() / 2), self.rect.y + self.rect.h / 2 - (self.text.get_height() / 2)))

	# override me
	def onclick(self):
		print("clicked button ", self)

	def checkHover(self, mousePos):
		self.hovering = self.rect.collidepoint(mousePos)		
