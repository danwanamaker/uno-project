import deck_functions as df


def construct_hand():
    result_hand = []
    for i in range(7):
        result_hand.append(df.choose_card())
    return result_hand

def draw_card(hand):
    output_hand = hand.copy()
    card_to_add = df.choose_card()
    output_hand.append(card_to_add)
    return output_hand

# print(construct_hand())