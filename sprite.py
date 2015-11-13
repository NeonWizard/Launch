class Sprite(object):
	def __init__(self, images):
		self.images = images
		if type(images).__name__ == pygame.Surface:
			self.images = [images]