import items
import sentientBeings
import textwrap


class MapTile(object):
	""" Base Map tile class"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def 


class StartingRoom(MapTile):
	def intro_text(self):
		return textwrap.fill("You are outside of a cave. In front of you there are several human skulls impaled with wooden sticks. This must be the orc lair you are looking for.")

a = StartingRoom(0,1)
print(a.intro_text())