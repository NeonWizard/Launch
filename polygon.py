class Polygon:
	def __init__(self, points, color):
		self.points = points
		self.color = color

	def draw(self, surface):
		pygame.draw.polygon(surface, self.points, self.color)