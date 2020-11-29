import deck_functions as df


def admonish(card1, card2):
    color = ''
    if card2[1] == 'f' or card2[1] == 'w':
        color = decode_color(card2)
    card1_eng = decode(card1)
    card2_eng = decode(card2)
    if color != '':
        print('You can\'t play a {} on a {} Wild card!'.format(card1_eng, color))
    else:
        print('You can\'t play a {} on a {}!'.format(card1_eng, card2_eng))


def construct_hand():
    result_hand = []
    for i in range(7):
        result_hand.append(df.choose_card())
    result_hand.sort()
    return result_hand


def decode(card):
    color = decode_color(card)
    if card[1] == 'r':  # Generate the second part of the English name of the card.
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


def draw_rules():
    print('House rule: How should drawing work?')
    print('  1. Keep drawing until you get a card you can play.')
    print('  2. Draw one card and your turn is over.')
    rule = input('--> ')
    while True:
        if rule == '1':
            print()
            return False
        elif rule == '2':
            print()
            return True
        else:
            print('Please choose one of the two house rules.')
            rule = input('--> ')


def is_legal(card1, card2):  # card1 is the card we are checking legality on, card2 is what we're checking against.
    if card1[0] == 'w':  # Check if they played a Wild card.
        return True
    elif card1[0] == card2[0]:  # Check if the colors of two cards match.
        return True
    elif card1[1] == card2[1]:  # Check if the numbers of two cards match.
        return True
    else:
        return False


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


def skip_rules():
    print('House rule: Someone plays a Draw 2 or Draw 4 on you. What happens next?')
    print('  1. You Draw 2 or Draw 4, and then go ahead with your turn like normal.')
    print('  2. You Draw 2 or Draw 4, and then your turn ends.')
    rule = input('--> ')
    while True:
        if rule == '1':
            print()
            return False
        elif rule == '2':
            print()
            return True
        else:
            print('Please choose one of the two house rules.')
            rule = input('--> ')
