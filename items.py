from itertools import count

class Item(object):
	"""Base item class"""
	def __init__(self, name, description, value):
		super(Item, self).__init__()
		self.name = name
		self.description = description
		self.value = value
		self.pickable = True

	def hasArmorAttribute(self):
		try:
			return self.ac >= 0
		except Exception as e:
			return False

	def __str__(self):
		return f"{'-'*44}\n{self.name}\n\nDescription: {self.description}\nValue: {self.value} gold\n{'-'*44}"


class Currency(Item):
	"""Gold piece"""
	_count = 0
	def __init__(self, currency_type, amount):
		self.amount = amount
		Currency._count += self.amount
		self.currency_type = currency_type
		super(Currency, self).__init__(name = currency_type,
			description = f'{self.amount} round shiny coins of {self.currency_type}',
			value = self.currency_converter())		

	def currency_converter(self):
		if self.currency_type == 'Platinum':
			return self.amount * 10
		if self.currency_type == 'Gold':
			return self.amount
		if self.currency_type == 'Silver':
			return self.amount / 10
		if self.currency_type == 'Copper':
			return self.amount / 100


class Weapon(Item):
	"""Weapon base class"""
	def __init__(self, name, description, value, damage, type):
		self.damage = damage
		self.type = type
		self.slot = 'r_hand'
		super(Weapon, self).__init__(name, description, value)

	def __str__(self):
		return f"{'-'*44}\n{self.name}({self.type})({self._count})\n\nDescription: {self.description}\nDamage: {self.damage}\nValue: {self.value}\n{'-'*44}"


class Armor(Item):
	"""Armor base class"""
	def __init__(self, name, description, value, ac, type, dex_max, str_restriction, stealth_restriction):
		super(Armor, self).__init__(name, description, value)
		self.name = name
		self.description = description
		self.value = value
		self.ac = ac
		self.type = type
		self.dex_max = dex_max
		self.str_restriction = str_restriction
		self.stealth_restriction = stealth_restriction

	def __str__(self):
		self.dex_mod = f"+ Dex modifier (max: {self.dex_max})" if self.dex_max != "0" else ""
		return (f"{'-'*44}\n{self.name} ({self.type})\n\nDescription: {self.description}\n"
		f"Armor Class: {self.ac} {self.dex_mod}\n"
		f"Strength needed: {self.str_restriction}\nStealth: {self.stealth_restriction}\n"
		f"Value: {self.value}\n{'-'*44}")


class Shield(Item):
	_count = 0
	def __init__(self):
		Shield._count += 1
		self.ac = 2
		self.type = 'Shield'
		self.slot = 'l_hand'
		self.dex_max = '-'
		super().__init__(name = "Shield",
			description = "Shield is a piece of personal armor held in the hand.",
			value = 10)


class AssassinSuit(Armor):
	"""Assassin Suit Armor class"""
	_count = 0
	def __init__(self):
		AssassinSuit._count += 1
		self.slot = 'body'
		super(AssassinSuit, self).__init__(name = 'Assassin Suit',
			description = 'An assassin suit is built for the kill, made of damage resistant fabric. This suit is equipped with toe spikes, so your speed is not reduced when climbing on surfaces that the spikes can grip, such as if the wall is soft like dirt or wood, cracked, etc.',
			value = 500,
			ac = 12,
			type = 'Light Armor',
			dex_max = '-',
			str_restriction = '-',
			stealth_restriction = '-')

class Chain_mail(Armor):
	_count = 0
	def __init__(self):
		Chain_mail._count += 1
		self.slot = 'body'
		super().__init__(name = 'Chain Mail',
			description = "Chain mail is a type of armor consisting of small metal rings linked together in a pattern to form a mesh",
			value = 75,
			ac = 16,
			type = 'Heavy Armor',
			dex_max = "0",
			str_restriction = 13,
			stealth_restriction = "disadvantage")





		
		

class Rock(Item):
	"""Just a rock"""
	_count = 0
	def __init__(self):
		Rock._count += 1
		super(Rock, self).__init__(name = 'Rock',
			description = "It's just a rock",
			value = 0)


class Dagger(Weapon):
	"""Dagger class"""
	_count = 0
	def __init__(self):
		Dagger._count += 1
		super(Dagger, self).__init__(name = 'Dagger',
			description = 'A small dagger',
			damage = 'd4',
			type = 'Simple Melee Weapon',
			value = 2)
		

class Scimitar(Weapon):
	"""Scimitar class"""
	_count = 0
	def __init__(self):
		Scimitar._count += 1
		super(Scimitar, self).__init__(name = 'Scimitar',
			description = 'A backsword with a curved blade',
			damage = 'd6',
			type = 'Martial Melee Weapon',
			value = 25)

		

		