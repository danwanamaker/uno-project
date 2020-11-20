import deck_functions as df
import hand_functions as hf


class Player:
    def __init__(self, order, player_name):
        self.name = player_name
        self.number = int(order)
        self.hand = hf.construct_hand()

    def __str__(self):
        return 'Player ' + str(self.number) + ': ' + self.name + ' holding ' + str(len(self.hand)) + ' cards'

    def draw_card(self):
        output_hand = self.hand.copy()
        output_hand.append(df.choose_card())
        self.hand = output_hand


def setup_players():  # gets names of players and returns them in a list
    players = []
    num_players = 1
    while True:
        print('Enter player {}\'s name or type "done" if all players are entered: ' \
              .format(num_players), end='')
        player_name = input()
        if player_name == 'done':
            break
        else:
            players.append(Player(num_players, player_name))
        num_players += 1
    return players
