import pygame
import random

TRANSPARENCY = pygame.Color(0, 0, 0, 0)

def generateHills(surfSize, hills):
	surf = pygame.Surface(surfSize).convert_alpha()

	surf.fill(TRANSPARENCY)

	toBlit = []

	for i in range(hills):
		radius = random.randrange(surfSize[0]/hills, surfSize[0]/hills*1.5)
		pos = (surfSize[0]/hills*i+random.randrange(-50, 0)*2+100, surf.get_height()+radius/2)
		toBlit.append(((0, 255, 0), pos, radius))

	random.shuffle(toBlit)

	for i in toBlit:
		pygame.draw.circle(surf, i[0], i[1], i[2])
		pygame.draw.circle(surf, (0, 0, 0), i[1], i[2]+1, 1)


	return surf