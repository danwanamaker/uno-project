import deck_functions as df
import hand_functions as hf
import player_functions as pf
import random


def hello():
	print('Hello world')


p1_hand = []
my_deck = df.premade_deck
print(df.choose_card())
my_hand = hf.construct_hand()
print(my_hand)
my_hand = hf.draw_card(my_hand)
print(my_hand)

player_1 = pf.player(1, 'Dan')
print(player_1)
print(player_1.hand)
player_1.draw_card()
print(player_1.hand)
