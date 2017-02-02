class Item(object):
	"""Base item class"""
	def __init__(self, name, description, value):
		super(Item, self).__init__()
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return f"{'-'*44}\n{self.name}\n\nDescription: {self.description}\nValue: {self.value} gold\n{'-'*44}"


class Currency(Item):
	"""Gold piece"""
	def __init__(self, currency_type, amount):
		self.amount = amount
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
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super(Weapon, self).__init__(name, description, value)

	def __str__(self):
		return f"{'-'*44}\n{self.name}\n\nDescription: {self.description}\nDamage: {self.damage}\nValue: {self.value}\n{'-'*44}"


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
		return (f"{'-'*44}\n{self.name}({self.type})\n\nDescription: {self.description}\n"
		f"Armor Class: {self.ac} + Dex modifier (max: {self.dex_max})\n"
		f"Strength needed: {self.str_restriction}\nStealth: {self.stealth_restriction}\n"
		f"Value: {self.value}\n{'-'*44}")


class AssassinSuit(Armor):
	"""Assassin Suit Armor class"""
	def __init__(self):
		super(AssassinSuit, self).__init__(name = 'Assassin Suit',
			description = 'An assassin suit is built for the kill, made of damage resistant fabric. This suit is equipped with toe spikes, so your speed is not reduced when climbing on surfaces that the spikes can grip, such as if the wall is soft like dirt or wood, cracked, etc.',
			value = 500,
			ac = 12,
			type = 'Light Armor',
			dex_max = '-',
			str_restriction = '-',
			stealth_restriction = '-')

		
		

class Rock(Item):
	"""Just a rock"""
	def __init__(self):
		super(Rock, self).__init__(name = 'Rock',
			description = "It's just a rock",
			value = 0)


class Dagger(Weapon):
	"""Dagger class"""
	def __init__(self):
		super(Dagger, self).__init__(name = 'Dagger',
			description = 'A small dagger',
			damage = 'd4',
			value = 2)
		

		