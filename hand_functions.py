import deck_functions as df


def construct_hand():
    result_hand = []
    for i in range(7):
        result_hand.append(df.choose_card())
    return result_hand


def decode(card):
    color = ''
    number = ''
    if card[0] == 'r':  # Generate the first part of the English name of the card.
        color = 'Red'
    elif card[0] == 'y':
        color = 'Yellow'
    elif card[0] == 'g':
        color = 'Green'
    elif card[0] == 'b':
        color = 'Blue'
    if card[1] == 'r':  # Generate the second part.
        number = ' Reverse'  # Extra spaces are so we can concatenate without Wild coming out as 'Wild '.
    elif card[1] == 'd':
        number = ' Draw 2'
    elif card[1] == 's':
        number = ' Skip'
    elif card[1] == 'w':
        color, number = 'Wild', ''
    elif card[1] == 'f':
        color, number = 'Wild', ' Draw 4'
    else:
        number = ' ' + card[1]
    return color + number


# def draw_card(hand):
#     output_hand = hand.copy()
#     card_to_add = df.choose_card()
#     output_hand.append(card_to_add)
#     return output_hand
# moved to a method in Player class
