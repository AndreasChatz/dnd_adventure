import items
import sentientBeings





def main():
	# a = items.Item(name = 'pirouni', description = 'voithaei stin vrosi', value = 0.01)
	# print(a)
	# gold = items.Currency(currency_type = 'Silver', amount = 30)
	# print(gold)
	# rock = items.Rock()
	# print(rock)

	inventory = []
	dagger = items.Dagger()
	# print(dagger)
	# print('proto ',dagger.quantity)

	another_dagger = items.Dagger()
	dag = items.Dagger()
	# print(another_dagger)
	# print('deutero ',another_dagger.quantity)

	assassin_suit = items.AssassinSuit()
	print(assassin_suit)

	print(dag)

	scim = items.Scimitar()
	scimI = items.Scimitar()
	print(scim)

	cat = sentientBeings.Cat()
	print(cat.attributeModifier(cat.str))
	print(cat)
	brownBear = sentientBeings.BrownBear()
	print(brownBear)
	zombie = sentientBeings.Zombie()
	print(zombie)
	print(zombie.hasImmunityTo("poisoned"))
	print("zombie's initiative:",zombie.initiative)
	print("cat's initiative:",cat.initiative)


# def pick(item, inventory):
# 	inv_type = [type(i) for i in inventory]
# 	if type(item) not in inv_type:
# 		inventory.append(item)
# 	print(type(item))
# 	print(len(inventory))
# 	print(inventory[0])

if __name__ == "__main__":
	main()