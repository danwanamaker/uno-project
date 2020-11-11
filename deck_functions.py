colors = ['r', 'y', 'g', 'b']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 's', 'r', 'd']
master_deck = ['r0', 'y0', 'g0', 'b0']
wilds = ['ww', 'wd']

for i in range(2):
	for color in colors:
		for number in numbers:
			master_deck.append(color + number)
for i in range(4):
	for wild in wilds:
		master_deck.append(wild)

print(master_deck)
print(len(master_deck))