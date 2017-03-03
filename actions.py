from player import Player


class Action(object):
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.name = name
		self.hotkey = hotkey
		self.kwargs = kwargs

	def __str__(self):
		return f"{self.hotkey}:{self.name}"


class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name='Move north', hotkey='n')

class Quit(Action):
	def __init__(self):
		super().__init__(method=Player.quit, name='Quit game', hotkey='q')


class MoveSouth(Action):
	def __init__(self):
		super().__init__(method=Player.move_south, name='Move south', hotkey='s')


class MoveEast(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name='Move east', hotkey='e')


class MoveWest(Action):
	def __init__(self):
		super().__init__(method=Player.move_west, name='Move west', hotkey='w')


class ViewInventory(Action):
	"""Prints the player's inventory"""
	def __init__(self):
		super().__init__(method=Player.show_inventory, name='View inventory', hotkey='i')


class Quit(Action):
	def __init__(self):
		super().__init__(method=Player.quit, name='Quit game', hotkey='q')