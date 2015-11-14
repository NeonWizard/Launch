import pygame
import random

TRANSPARENCY = pygame.Color(0, 0, 0, 0)

def generateHills(surfSize, hills):
	surf = pygame.Surface(surfSize).convert_alpha()

	surf.fill(TRANSPARENCY)

	for i in range(hills):
		pygame.draw.circle(surf, [0, 255, 0], (surfSize[0]/hills*i+random.randrange(-50, 50), surf.get_height()), random.randrange(surfSize[0]/hills, surfSize[0]/hills*1.5))

	return surf