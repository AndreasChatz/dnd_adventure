import items
import sentientBeings
import player





def main():
	# a = items.Item(name = 'pirouni', description = 'voithaei stin vrosi', value = 0.01)
	# print(a)
	# gold = items.Currency(currency_type = 'Silver', amount = 30)
	# print(gold)
	# rock = items.Rock()
	# print(rock)

	# inventory = []
	# dagger = items.Dagger()
	# # print(dagger)
	# # print('proto ',dagger.quantity)

	# another_dagger = items.Dagger()
	# dag = items.Dagger()
	# # print(another_dagger)
	# # print('deutero ',another_dagger.quantity)

	# assassin_suit = items.AssassinSuit()
	# print(assassin_suit)

	# print(dag)

	# scim = items.Scimitar()
	# scimI = items.Scimitar()
	# print(scim)

	# cat = sentientBeings.Cat()
	# print(cat.attributeModifier(cat.str))
	# print(cat)
	# brownBear = sentientBeings.BrownBear()
	# print(brownBear)
	# zombie = sentientBeings.Zombie()
	# print(zombie)
	# print("immunity zombie",zombie.hasImmunityTo("poisoned"))
	# print("zombie's initiative:",zombie.initiative)
	# print("cat's initiative:",cat.initiative)
	# print("immunity cat",cat.hasImmunityTo("cold"))
	# print("resistance cat",cat.hasResistanceTo("death"))

	fighter = player.Player()
	print("is alive:",fighter.is_alive())
	fighter.show_inventory()
	sh = items.Currency("Gold",40)
	print('adding Scimitar')
	fighter.don_item('Scimitar')
	for x in fighter.wearing:
		print(x.name)
	print('adding Shield')
	fighter.don_item('Shield')
	for x in fighter.wearing:
		print(x.name)
	print('adding Dagger')
	fighter.don_item('Dagger')
	for x in fighter.wearing:
		print(x.name)
	print('adding Chain Mail')
	fighter.don_item('Chain Mail')
	for x in fighter.wearing:
		print(x.name)
	print('adding Chain Mail')
	fighter.don_item('Chain Mail')
	for x in fighter.wearing:
		print(x.name)
	fighter.show_inventory()



if __name__ == "__main__":
	main()