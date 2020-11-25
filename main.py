import deck_functions as df
import hand_functions as hf
import player_functions as pf
import random


def token_increment(num):
    if num == len(players) - 1:
        num = 0
    else:
        num += 1
    return num


players = [pf.Player(1, 'Dan'), pf.Player(2, 'Ethan'), pf.Player(3, 'Holton')]  # placeholder players
# players = pf.setup_players()  # actual player constructor
token = 0
last_card = df.choose_card()

while True:  # turn loop
    print('Player {}: {} you\'re up!'.format(token + 1, players[token].name))
    print('Last card played was a {}.'.format(hf.decode(last_card)))
    print(players[token].display_hand())
    print('What would you like to do?\n  1. Draw a card\n  2. Play a card\n--> ', end = '')
    prompt = input()
    if prompt == 'done':
        break
    token = token_increment(token)
