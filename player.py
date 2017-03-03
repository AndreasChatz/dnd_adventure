from sentientBeings import SentientBeing
import items
import world

class Player(SentientBeing):	
	"""Player class"""
	def __init__(self):
		super().__init__(cr=1,
			size="medium",race="Human",name="Pyth Agoras",alignment="Neutral evil",
			ac=10,hp=12,speed=30,
			str=16,dex=12,con=16,int=8,wis=14,cha=8)

		self.inventory = [items.Scimitar(), items.Dagger(), items.Chain_mail(), items.AssassinSuit(), items.Shield(), items.Currency("Gold",15)]

		# 1 arm slot, 1 body slot, 1 foot slot, 2 hand slots, 1 head slot,
		# 2 ring slots, 1 shoulder slot, 1 waist slot.
		self.wearing = {"arm":"", "body":"", "foot": "", "r_hand":"", "l_hand":"",
							"head":"", "ring_1":"", "ring_2":"", "shoulder":"", "waist":""}

		self.location_x, self.loaction_y = world.starting_position

	def is_alive(self):
		return self.hp > 0

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)

	def move(self, dx, dy):
		self.location_x += dx
		self.loaction_y += dy
		print(world.tile_exists(self.location_x, self.loaction_y).intro_text())

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):	
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

	def show_inventory(self):
		for item in reversed(self.inventory):
			print(f"{item.name}({item._count})", end="")
		print()

	def is_item_slot_available(self, item):
		return self.wearing[item.slot] == ""		

	# Given the name of an item, return the item object from the inventory or wearing.
	def get_item_given_a_name(self, item_name, from_data):

		# from_data could be the inventory list or the wearing dictionary.
		# if it is a dictionary copy the non string values (only the items)
		# to the data list
		data = [x for x in from_data.values() if x!= ""] if isinstance(from_data, dict) else from_data

		for item in data:
			if (item.name == item_name):
				return item
		return None

	def don_item(self, item_name):

		item = self.get_item_given_a_name(item_name, self.inventory)

		if (item == None):
			print('There is no such item in you inventory.')
			return

		if (self.is_item_slot_available(item)):
			self.wearing[item.slot] = item
			self.inventory.remove(item)
			self.calculateAC()
		else:
			print('Not available slot. Doff an item from the corresponding slot and try again.')

	def doff_item(self, item_name):
		item = self.get_item_given_a_name(item_name, self.wearing)

		if (item == None):
			print('You are not wearing this item.')
			return

		self.wearing[item.slot] = ""
		self.inventory.append(item)
		self.calculateAC()

	def calculateAC(self):
		ac_bonus_from_dex = self.attributeModifier(self.dex)
		sum_items_ac = 0 if self.wearing['body'] !="" else 10

		for item in self.wearing.values():
			if items.Item.hasArmorAttribute(item):
				if item.dex_max == 0:
					ac_bonus_from_dex = 0
				elif item.dex_max != "-":
					if int(item.dex_max) <= ac_bonus_from_dex:
						ac_bonus_from_dex = int(item.dex_max)
				sum_items_ac += item.ac
		
		self.ac = sum_items_ac + ac_bonus_from_dex
