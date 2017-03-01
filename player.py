from sentientBeings import SentientBeing
import items

class Player(SentientBeing):	
	"""Player class"""
	def __init__(self):
		super().__init__(cr=1,
			size="medium",race="Human",name="Pyth Agoras",alignment="Neutral evil",
			ac=10,hp=12,speed=30,
			str=16,dex=12,con=16,int=8,wis=14,cha=8)

		self.inventory = [items.Scimitar(), items.Dagger(), items.Chain_mail(), items.Shield(), items.Currency("Gold",15)]
		self.wearing = []

		# 1 arm slot, 1 body slot, 1 foot slot, 2 hand slots, 1 head slot,
		# 2 ring slots, 1 shoulder slot, 1 waist slot.
		self.items_slots = []

	def is_alive(self):
		return self.hp > 0

	def show_inventory(self):
		for item in self.inventory:
			print(f"{item.name}({item._count})", end="")
		print()

	def is_item_slot_available(self, item):
		item_class_name = item.__class__.__name__
		wearing_items_class_names = [x.__class__.__name__ for x in self.wearing]
		if (item.slot not in self.items_slots):
			return True
		else:
			if (isinstance(item, items.Shield)):
				return True if item_class_name not in wearing_items_class_names and self.items_slots.count('hand') < 2 else False
			elif (isinstance(item, items.Weapon)):
				return True if self.items_slots.count('hand') < 2 else False		

	# Given the name of an item, return the item object from the inventory.
	def get_item_given_a_name(self, item_name, fromlist):
		for item_inventory in fromlist:
			if (item_inventory.name == item_name):
				return item_inventory
		else:
			return None

	def don_item(self, item_name):
		if (len(self.wearing) > 10):
			print('All the slots are filled', 
				'Doff an item from the corresponding slot and try again.')

		item = self.get_item_given_a_name(item_name, self.inventory)

		if (item == None):
			print('There is no such item in you inventory.')
			return

		if (self.is_item_slot_available(item)):
			self.wearing.append(item)
			self.items_slots.append(item.slot)
			self.inventory.remove(item)
		else:
			print('Not available slots. Doff an item from the corresponding slot and try again.')

	def doff_item(self, item_name):
		item = self.get_item_given_a_name(item_name, self.wearing)

		if (item == None):
			print('You are not wearing this item.')
			return



	def calculateAC(self):
		add_items_ac = 0
		ac_bonus_from_dex = self.attributeModifier(self.dex)
		for item in self.wearing:
			if isinstance(item, items.Armor):
				if item.dex_max == 0:
					ac_bonus_from_dex = 0
				elif item.dex_max != "-":
					if int(item.dex_max) <= ac_bonus_from_dex:
						ac_bonus_from_dex = int(item.dex_max)

				add_items_ac += item.ac

		self.ac = ac_bonus_from_dex + add_items_ac


