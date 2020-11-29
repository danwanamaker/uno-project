import random


colors = ['r', 'y', 'g', 'b']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 's', 'r', 'd']  # s = skip, r = reverse, d = draw 2
starting_deck = ['r0', 'y0', 'g0', 'b0', 'ww', 'ww', 'ww', 'ww', 'wf', 'wf', 'wf', 'wf']
#  Red zero, yellow zero, green zero, blue zero, wild x4, wild draw 4 x4


def construct_deck():
    full_deck = starting_deck
    for i in range(2):
        for color in colors:
            for number in numbers:
                full_deck.append(color + number)
    return full_deck


master_deck = construct_deck()
premade_deck = ['r0', 'y0', 'g0', 'b0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'rs', 'rr', 'rd', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'ys', 'yr', 'yd', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'gs', 'gr', 'gd', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'bs', 'br', 'bd', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'rs', 'rr', 'rd', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'ys', 'yr', 'yd', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'gs', 'gr', 'gd', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'bs', 'br', 'bd', 'ww', 'wf', 'ww', 'wf', 'ww', 'wf', 'ww', 'wf']


def choose_card():
    card = random.choice(premade_deck)
    premade_deck.remove(card)
    return card


if __name__ == '__main__':
    # master_deck = construct_deck()
    print(premade_deck)
    print(len(premade_deck))
    print(random.random())
    print(choose_card())
    print(len(premade_deck))
    my_hand = ['b3', 'y4', 'g5']
    print(my_hand)
    my_hand.append(choose_card())
    print(my_hand, len(premade_deck))


