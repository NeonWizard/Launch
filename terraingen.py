import pygame
import random

TRANSPARENCY = (0, 0, 0, 0)

def generateHills(surfSize, hills, background):
	surf = pygame.Surface(surfSize).convert_alpha()

	surf.fill(background)

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
		return generateHills(surfSize, hills, (155, 255, 255)), (155, 255, 255)
	elif layer <= 20: # 1
		surf = pygame.Surface(surfSize).convert_alpha()
		surf.fill(TRANSPARENCY)
		#surf.fill((155-layer*4, 255-layer*10, 255-layer*8))
		return surf, (155-layer*4, 255-layer*10, 255-layer*8)
	elif layer <= 30: # star intro
		surf = pygame.Surface(surfSize).convert_alpha()
		surf.fill(TRANSPARENCY)
		#surf.fill((71, 45, 87))

		for i in range(50):
			pygame.draw.circle(surf, (255,255,255), (int(random.gauss(surfSize[0]/2, surfSize[0])), int(random.gauss(surfSize[1]/2, surfSize[1]))), 3)

		return surf, (71, 45, 87)
	elif layer <= 100:
		surf = pygame.Surface(surfSize)
		surf.fill((255, 255, 0))
		return surf, (255, 255, 0)
