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
		pass

	def toChar(self, num):
		try:
			return ALPHABET[num-97]
		except:
			print("Non ascii key")