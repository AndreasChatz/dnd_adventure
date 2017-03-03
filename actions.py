import player


class Action(object):
	def __init__(self, method, hotkey, name, **kwargs):
		self.mehtod = mehtod
		self.hotkey = hotkey
		self.name = name
		self.kwargs = kwargs

	def __str__(self):
		return f"{self.hotkey}:{self.name}"


class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=player.move_north, name='Move north', hotkey='n')


class MoveSouth(Action):
	def __init__(self):
		super().__init__(method=player.move_south, name='Move south', hotkey='s')


class MoveEast(Action):
	def __init__(self):
		super().__init__(method=player.move_east, name='Move east', hotkey='e')


class MoveWest(Action):
	def __init__(self):
		super().__init__(method=player.move_west, name='Move west', hotkey='w')


class ViewInventory(Action):
	"""Prints the player's inventory"""
	def __init__(self):
		super().__init__(method=player.show_inventory, name='View inventory', hotkey='i')