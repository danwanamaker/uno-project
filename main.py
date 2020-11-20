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


players = [pf.Player(1, 'Dan'), pf.Player(2, 'Holton'), pf.Player(3, 'Barry')]
    # players = pf.setup_players()
token = 0

while True:  # turn loop
    print('Player {}: {} you\'re up!'.format(token + 1, players[token].name))
    prompt = input('What would you like to do?\n  1. Draw a card\n  2. Play a card\n--> ')
    if prompt == 'done':
        break
    token = token_increment(token)
