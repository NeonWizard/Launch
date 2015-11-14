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

	pygame.draw.circle(surf, (0, 255, 0), (0, surfSize[1]), int(surfSize[0]/hills*.75))
	pygame.draw.circle(surf, (0, 255, 0), (surfSize[0], surfSize[1]), int(surfSize[0]/hills*.75))

	pygame.draw.circle(surf, (0, 0, 0), (0, surfSize[1]), int(surfSize[0]/hills*.75+1), 1)
	pygame.draw.circle(surf, (0, 0, 0), (surfSize[0], surfSize[1]), int(surfSize[0]/hills*.75+1), 1)

	return surf

def generateLayer(layer, surfSize, hills):
	if layer == 0: # hills
		return generateHills(surfSize, hills)
	elif layer <= 10: # test
		surf = pygame.Surface(surfSize)
		surf.fill((255, 0, 0))
		return surf
	elif layer <= 20: # test
		surf = pygame.Surface(surfSize)
		surf.fill((0, 255, 0))
		return surf
	elif layer <= 100: # sky
		surf = pygame.Surface(surfSize)
		surf.fill((255, 255, 0))
		return surf
