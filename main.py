import deck_functions as df
import random


def hello():
	print('Hello world')


p1_hand = []
my_deck = df.premade_deck
print(my_deck)
print(len(my_deck))
print(random.choice(my_deck))
print(df.draw_card())
