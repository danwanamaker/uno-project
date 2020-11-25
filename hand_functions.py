import deck_functions as df


def construct_hand():
    result_hand = []
    for i in range(7):
        result_hand.append(df.choose_card())
    result_hand.sort()
    return result_hand


def decode_color(card):
    color = ''
    if card[0] == 'r':  # Generate the first part of the English name of the card.
        color = 'Red'
    elif card[0] == 'y':
        color = 'Yellow'
    elif card[0] == 'g':
        color = 'Green'
    elif card[0] == 'b':
        color = 'Blue'
    return color


def decode(card):
    color = decode_color(card)
    decoded = ''
    if card[1] == 'r':  # Generate the second part.
        decoded = color + ' Reverse'
    elif card[1] == 'd':
        decoded = color + ' Draw 2'
    elif card[1] == 's':
        decoded = color + ' Skip'
    elif card[1] == 'w':
        if color == '':
            decoded = 'Wild'
        else:
            decoded = 'Wild (play {})'.format(color)
    elif card[1] == 'f':
        if color == '':
            decoded = 'Wild Draw 4'
        else:
            decoded = 'Wild Draw 4 (play {})'.format(color)
    else:
        decoded = color + ' ' + card[1]
    return decoded


def readout(hand):
    output = ''
    count = 2
    for card in hand:
        english = decode(card)
        output += english
        if count < len(hand):
            output += ', '
        elif count == len(hand):
            output += ', and '
        count += 1
    return output


def is_legal(card1, card2):  # card1 is the card we are checking legality on, card2 is what we're checking against.
    if card1[0] == 'w':  # Check if they played a Wild card.
        return True
    elif card1[0] == card2[0]:  # Check if the colors of two cards match.
        return True
    elif card1[1] == card2[1]:  # Check if the numbers of two cards match.
        return True
    else:
        return False


def read_last(card, wild):
    if wild == '':
        print('Last card played was a {}.'.format(decode(card)))
    else:
        print('Last card played was a {} (play {}).'.format(decode(card), decode_color(wild)))


def admonish(card1, card2, wild):
    if wild == '':
        print('You can\'t play a {} on a {}!'.format(card1, card2))
    else:
        print('You can\'t play a {} on a {} Wild card!'.format(card1, decode_color(wild)))


print(is_legal('ww', 'y3'))

# def draw_card(hand):
#     output_hand = hand.copy()
#     card_to_add = df.choose_card()
#     output_hand.append(card_to_add)
#     return output_hand
# moved to a method in Player class
