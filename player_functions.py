import deck_functions as df
import hand_functions as hf

class player:
    def __init__(self, order, player_name):
        self.name = player_name
        self.number = int(order)
        self.hand = hf.construct_hand()

    def __str__(self):
        return('Player ' + str(self.number) + ': ' + self.name)

    def draw_card(self):
        output_hand = self.hand.copy()
        output_hand.append(df.choose_card())
        self.hand = output_hand