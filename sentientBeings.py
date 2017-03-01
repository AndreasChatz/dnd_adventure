
class SentientBeing(object):
	def __init__(self, cr, size, race, name, alignment, ac, hp, speed, str, dex, con, int, wis, cha):
		self.cr = cr
		self.size = size
		self.race = race
		self.name = name
		self. alignment = alignment
		self.ac = ac
		self.hp = hp
		self.speed = speed

		self.str = str
		self.dex = dex
		self.con = con
		self.int = int
		self.wis = wis
		self.cha = cha

		self.immunities = []
		self.resistances = []

		self.bonusInitiative = 0
		self.initiative = self.attributeModifier(dex) + self.bonusInitiative


	def attributeModifier(self, attribute):
		return attribute // 2 - 5

	def hasImmunityTo(self, type):
		return True if type in self.immunities else False

	def hasResistanceTo(self, type):
		return True if type in self.resistances else False

	def hasSense(self, type):
		return True if type in self.senses else False

	def __str__(self):
		return f"It's a {self.size} {self.race}."


class Cat(SentientBeing):
	"""Cat class"""
	def __init__(self):
		super().__init__(cr=0,
			size="tiny",race="beast",name="psipsinel",alignment="unaligned",
			ac=12,hp=2,speed=40,
			str=3,dex=15,con=10,int=3,wis=12,cha=7)

		self.stealth = 4
		self.toHit = 0
		self.dmg = 1
		self.perseption = 3
		self.passivePers = 13
		self.resistances = ["death"]
		

class BrownBear(SentientBeing):
	def __init__(self):
		super().__init__(cr=1,
			size="large",race="beast",name="",alignment="unaligned",
			ac=11,hp=34,speed=40,
			str=19,dex=10,con=16,int=2,wis=13,cha=7)

		self.toHit=[5,5]
		self.dmg=["d8","2d6"]
		self.perseption=3
		self.passivePers=13


class Zombie(SentientBeing):
	def __init__(self):		
		super().__init__(cr=0.25,
			size="medium",race="undead",name="",alignment="neutral evil",
			ac=8,hp=22,speed=20,
			str=13,dex=6,con=16,int=3,wis=6,cha=5,)

		self.saveWis = 0
		self.immunities = ["poison","poisoned"]
		self.senses = ["darkvision"]
		self.toHit = 4
		self.dmg = ["d6"] 
		self.perseption = 3
		self.passivePers = 13
