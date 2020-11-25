import deck_functions as df
import hand_functions as hf
import player_functions as pf


class Token:
    def __init__(self):
        self.count = 0
        self.last_card = ''
        self.is_reversed = False
        self.is_skipped = False
        self.is_draw_two = False
        self.is_draw_four = False
        self.wild_color = ''

    def __str__(self):
        return 'Player ' + str(len(players)) + ': ' + players[self.count].name + ' is up!'


def token_increment(num):
    if num == len(players) - 1:
        num = 0
    else:
        num += 1
    return num


# SETUP
players = [pf.Player(1, 'Dan'), pf.Player(2, 'Ethan'), pf.Player(3, 'Holton')]  # placeholder players
# players = pf.setup_players()  # actual player constructor
token = 0
my_token = Token()
last_card = df.choose_card()
while last_card[0] == 'w':  # So that we don't start the game with a Wild card.
    last_card = df.choose_card()

print(my_token)

# GAMEPLAY LOOP
while True:
    print('Player {}: {} you\'re up!'.format(token + 1, players[token].name))
        # players[token] is how we refer to the player whose turn it is.
    print('You\'re holding: ' + players[token].display_hand() + '.')
    print('Last card played was a {}.'.format(hf.decode(last_card)))
    # ONE PLAYER'S TURN LOOP
    while True:
        print('What would you like to do?')
        print('  1. Draw a card\n  2. Play a card\n--> ', end='')
        prompt = input()
        if prompt == '1':  # Draw a card
            players[token].draw_card()
            print('You drew a {}.'.format(players[token].new_card))
            print('You\'re now holding: ' + players[token].display_hand() + '.')
            print('Last card played was a {}.'.format(hf.decode(last_card)))
        elif prompt == '2':  # Play a card
            print('Choose a card:')
            players[token].list_hand()
            chosen_index = int(input('--> ')) - 1
            chosen_card = players[token].hand[chosen_index]
            if not hf.is_legal(chosen_card, last_card):
                print('You can\'t play a {} on a {}!'.format(hf.decode(chosen_card), hf.decode(last_card)))
            else:
                print('You played: ' + hf.decode(chosen_card))
                last_card = chosen_card
                players[token].hand.remove(chosen_card)
                print(players[token].display_hand())
        elif prompt == 'd2':
            players[token].draw_two()
        elif prompt == 'done':  # End turn
            break
        elif prompt == 'exit':
            break
    if prompt == 'exit':
        break
    token = token_increment(token)
