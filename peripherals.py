import string

ALPHABET = string.ascii_lowercase

class MouseInfo:
	def __init__(self, initPos):
		self.updatePos(initPos)

	def updatePos(self, pos):
		self.x = pos[0]
		self.y = pos[1]

class KeyInfo:
	def __init__(self):
		self.keysDown = []

	def handle(self, num):
		self.keysDown.append(Key(num))

class Key:
	def __init__(self, num):
		self.char = ALPHABET[num-97]
		print self.char