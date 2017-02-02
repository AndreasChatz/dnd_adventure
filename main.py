import items

def main():
	a = items.Item(name = 'pirouni', description = 'voithaei stin vrosi', value = 0.01)
	print(a)
	gold = items.Currency(currency_type = 'Silver', amount = 30)
	print(gold)
	rock = items.Rock()
	print(rock)
	dagger = items.Weapon(name = 'Dagger', description = 'A small dagger', damage = 'd4', value = 0.2)
	print(dagger)
	another_dagger = items.Dagger()
	print(another_dagger)
	assassin_suit = items.AssassinSuit()
	print(assassin_suit)



if __name__ == "__main__":
	main()