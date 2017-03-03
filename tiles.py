import items
import sentientBeings
import actions
import world
import textwrap


class MapTile(object):
	""" Base Map tile class"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def adjacent_move(self):
		"""Returns all move actions for adjacent tiles."""
		moves = []
		if world.tile_exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y -1):
			moves.append(actions.MoveNorth)
		if world.tile_exists(self.x, self.y + 1):
			moves.append(actions.MoveSouth)
		return moves

	def available_actions(self):
		"""Returns all of the available actions in this room."""
		moves = self.adjacent_move()
		moves.append(actions.ViewInventory())

		return moves

class StartingRoom(MapTile):
	def intro_text(self):
		return textwrap.fill("You are outside of a cave. In front of you there are several human skulls impaled with wooden sticks. This must be the orc lair you are looking for.")

a = StartingRoom(0,1)
print(a.intro_text())