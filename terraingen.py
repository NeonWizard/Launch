import pygame

TRANSPARENCY = pygame.Color(0, 0, 0, 0)

def generateHills():
	surf = pygame.Surface(config.SCREEN_SIZE).convert_alpha()

	self.bleh = pygame.Surface((config.SCREEN_SIZE)).convert_alpha()
	self.bleh.fill(TRANSPARENCY)

	hills = 10
	for i in range(hills):
		pygame.draw.circle(self.bleh, [0, 255, 0], (config.SCREEN_SIZE[0]/hills*i+random.randrange(-50, 50), self.bleh.get_height()), random.randrange(config.SCREEN_SIZE[0]/hills, config.SCREEN_SIZE[0]/hills*1.5))
			