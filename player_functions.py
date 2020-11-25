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

    def display_hand(self):
        readout = 'You\'re holding: '
        count = 2
        for card in self.hand:
            english = hf.decode(card)
            readout += english
            if count < len(self.hand):
                readout += ', '
            elif count == len(self.hand):
                readout += ', and '
            count += 1
        readout += '.'
        return readout


def setup_players():  # gets names of players and returns them in a list
    players_list = []
    num_players = 1
    while True:
        print('Enter player {}\'s name or type "done" if all players are entered: ' \
              .format(num_players), end='')
        player_name = input()
        if player_name == 'done':
            break
        else:
            players_list.append(Player(num_players, player_name))
        num_players += 1
    return players_list
