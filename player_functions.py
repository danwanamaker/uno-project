import deck_functions as df
import hand_functions as hf


class Player:
    def __init__(self, order, player_name):
        self.name = player_name
        self.number = int(order)
        self.hand = hf.construct_hand()
        self.new_card = ''
        self.uno = False

    def __str__(self):
        return 'Player ' + str(self.number) + ': ' + self.name + ' holding ' + str(len(self.hand)) + ' cards'

    def draw_card(self):
        output_hand = self.hand.copy()
        self.new_card = df.choose_card()
        output_hand.append(self.new_card)
        output_hand.sort()
        self.new_card = hf.decode(self.new_card)
        self.hand = output_hand

    def display_hand(self):
        readout = ''
        count = 2
        for card in self.hand:
            english = hf.decode(card)
            readout += english
            if count < len(self.hand):
                readout += ', '
            elif count == len(self.hand):
                readout += ', and '
            count += 1
        return readout

    def draw_two(self):
        new_cards = []
        for i in range(2):
            new_cards.append(df.choose_card())
        print('Draw 2! You drew: {} and {}.'.format(hf.decode(new_cards[0]), hf.decode(new_cards[1])))
        self.hand.extend(new_cards)
        self.hand.sort()
        print('You\'re now holding: ' + self.display_hand() + '.')

    def draw_four(self):
        new_cards = []
        for i in range(4):
            new_cards.append(df.choose_card())
        print('Draw 4! You drew: ' + hf.readout(new_cards))
        self.hand.extend(new_cards)
        self.hand.sort()
        print('You\'re now holding: ' + self.display_hand() + '.')

    def list_hand(self):
        i = 1
        for card in self.hand:
            print('  {}. {}'.format(i, hf.decode(card)))
            i += 1


def setup_players():  # Gets names of players and returns them in a list.
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
