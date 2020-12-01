from tkinter import simpledialog
import deck_functions as df
import hand_functions as hf
import tkinter


class Player:
    def __init__(self, order, player_name):
        self.name = player_name
        self.number = int(order)
        self.hand = hf.construct_hand()
        self.new_card = ''
        self.uno = False

    def __str__(self):
        return 'Player ' + str(self.number) + ': ' + self.name + ' holding ' + str(len(self.hand)) + ' cards'

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

    def draw_card(self, read=False):
        output_hand = self.hand.copy()
        self.new_card = df.choose_card()
        if read:
            print('You drew a {}.'.format(hf.decode(self.new_card)))
        output_hand.append(self.new_card)
        output_hand.sort()
        self.new_card = hf.decode(self.new_card)
        self.hand = output_hand

    def draw_two(self):
        new_cards = []
        for i in range(2):
            new_cards.append(df.choose_card())
        print('Draw 2! You drew: {} and {}.'.format(hf.decode(new_cards[0]), hf.decode(new_cards[1])))
        self.hand.extend(new_cards)
        self.hand.sort()
        # self.now_holding()

    def draw_four(self):
        new_cards = []
        for i in range(4):
            new_cards.append(df.choose_card())
        print('Draw 4! You drew: ' + hf.readout(new_cards))
        self.hand.extend(new_cards)
        self.hand.sort()
        # self.now_holding()

    def holding(self):
        print('You\'re holding: {}.'.format(self.display_hand()))

    def now_holding(self):
        print('You\'re now holding: {}.'.format(self.display_hand()))

    def list_hand(self):
        i = 1
        for card in self.hand:
            print('  {}. {}'.format(i, hf.decode(card)))
            i += 1

    def play_card(self):
        print('Choose a card to play (or enter 0 to draw a card):')
        self.list_hand()
        while True:
            try:
                chosen_index = int(input('--> ')) - 1
            except ValueError:
                print('Please choose a valid card. ', end='')
                continue
            else:
                break
        # chosen_index = int(input('--> ')) - 1
        while True:
            if chosen_index in range(-1, len(self.hand)):
                break
            else:
                print('Please choose a valid card.')
                chosen_index = int(input('--> ')) - 1
        return chosen_index


class Token:
    def __init__(self, list_of_players):
        self.count = 0
        self.draw_one_rule = hf.draw_rules()
        self.game_over = False
        self.last_card = ''
        self.is_draw_four = False
        self.is_draw_two = False
        self.is_first_reversed = False
        self.is_reversed = False
        self.is_skipped = False
        self.list_players = list_of_players
        self.skip_after_draw = hf.skip_rules()

    def __str__(self):
        return 'Player ' + str(len(self.list_players)) + ': ' + self.list_players[self.count].name + ' is up!'

    def increment(self):
        if not self.is_reversed:  # For normal play, go to next player in the list
            if self.count == len(self.list_players) - 1:  # Unless you're at the end of the list
                self.count = 0  # In which case you start over
            else:
                self.count += 1
        else:  # If play is reversed, go backwards unless you are at the start of the list.
            if self.count == 0:
                self.count = len(self.list_players) - 1
            else:
                self.count -= 1


def setup_players():  # Gets names of players and returns them in a list.
    players_list = []
    num_players = 1
    while True:
        player_name = simpledialog.askstring('Enter name',
                'Enter Player {}\'s name (or type "done" if all players are entered):'.format(num_players))
        # print('Enter player {}\'s name or type "done" if all players are entered: '
        #       .format(num_players), end='')
        # player_name = input()
        if player_name == 'done':
            break
        else:
            players_list.append(Player(num_players, player_name))
        num_players += 1
    for player in players_list:
        print(player)
    return players_list
