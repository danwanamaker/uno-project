import deck_functions as df


def construct_hand():
    result_hand = []
    for i in range(7):
        result_hand.append(df.draw_card())
    return result_hand

# print(construct_hand())