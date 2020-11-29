import deck_functions as df
import hand_functions as hf
import player_functions as pf


# SETUP
players = [pf.Player(1, 'Dan'), pf.Player(2, 'Ethan'), pf.Player(3, 'Holton')]  # placeholder players
# players = pf.setup_players()  # actual player constructor
token = pf.Token(players)
token.last_card = df.choose_card()
while token.last_card[0] == 'w' or token.last_card[1] == 'd' or token.last_card[1] == 's' or token.last_card[1] == 'r':
    df.premade_deck.append(token.last_card)
    token.last_card = df.choose_card()  # So that we don't start the game with a Wild/Skip/Draw/Reverse

print('If you have one card in your hand at the end of your turn, remember to declare UNO!\n'
      'When the game says, \'Type "end" to end your turn. -->\', this is where you should type "uno" instead.\n'
      'Otherwise you will have to Draw 2!\n')

# GAMEPLAY LOOP players[token.count] is how we refer to the player whose turn it is.
while not token.game_over:
    if token.is_skipped:  # Program will skip all actions for that player's turn.
        print(players[token.count].name + ', you\'re skipped this turn. Boo hoo, better luck next time!\n')
        token.is_skipped = False  # Clear skip action for next turn.
    else:
        if token.is_first_reversed:  # Give a special greeting to the person right after the reverse.
            print('Back to you, {}! '.format(players[token.count].name), end='')
            token.is_first_reversed = False  # Make it so it doesn't do that again.
        else:
            print('Player {}: {} you\'re up!'.format(token.count + 1, players[token.count].name))

        # ONE PLAYER'S TURN LOOP
        while True:
            if token.is_draw_two:
                players[token.count].draw_two()
                token.is_draw_two = False
                if token.skip_after_draw:
                    print('That\'s all for now. Next!\n')
                    break
            elif token.is_draw_four:
                players[token.count].draw_four()
                token.is_draw_four = False
                if token.skip_after_draw:
                    print('That\'s all for now. Next!\n')
                    break
            print('What would you like to do?')
            print('Last card played was a {}.'.format(hf.decode(token.last_card)))
            choice = players[token.count].play_card()
            if choice == -1:  # If they enter 0, this brings them back to the Turn Loop.
                players[token.count].draw_card(read=True)
                if token.draw_one_rule:  # When house rule is active, one card only draw and turn is over.
                    print()
                    break
                else:
                    continue
            chosen_card = players[token.count].hand[choice]  # Retrieve the card from their hand.
            if not hf.is_legal(chosen_card, token.last_card):  # Check that it's a legal play.
                hf.admonish(chosen_card, token.last_card)
            else:
                print('You played: ' + hf.decode(chosen_card) + '.')
                token.last_card = chosen_card  # Store the card that the player played
                if chosen_card[0] == 'w':  # Record any actions that affect the following player. vv
                    while True:
                        print('What color do you choose?')
                        print('r = Red | y = Yellow | g = Green | b = Blue')
                        wild = input('--> ')
                        if wild == 'r' or wild == 'y' or wild == 'g' or wild == 'b':
                            token.last_card = wild + chosen_card[1]
                            break
                        else:
                            print('Please choose a color.')
                if chosen_card[1] == 's':
                    token.is_skipped = True
                elif chosen_card[1] == 'r':
                    token.is_reversed = not token.is_reversed
                    token.is_first_reversed = True
                elif chosen_card[1] == 'd':
                    token.is_draw_two = True
                elif chosen_card[1] == 'f':
                    token.is_draw_four = True
                players[token.count].hand.remove(chosen_card)
                df.premade_deck.append(chosen_card)  # Discard the played card and return it to the deck.
                players[token.count].now_holding()
                ending = input('Type "end" to end your turn. --> ')
                if len(players[token.count].hand) == 1:
                    if ending.lower().strip() == 'uno':
                        print(players[token.count].name + ' declares UNO! Watch out!')
                    else:
                        print('You forgot to declare Uno, you fool! Draw 2 and try not to forget next time.')
                        players[token.count].draw_two()
                else:
                    if ending.lower().strip() == 'uno' and len(players[token.count].hand) > 1:
                        print('You wish you had Uno. Come back another time when you\'re not trippin.')
                if len(players[token.count].hand) == 0:
                    token.game_over = True
                print()
                break
            if choice == 'done':  # End turn
                print()
                break
    if token.game_over:
        break
    token.increment()

if token.game_over:
    print('Congratulations {}!! You are UNO champion of the day!'.format(players[token.count].name))
    for player in players:
        if player.name == players[token.count].name:
            continue
        print(player.name, end=', ')
    print('better luck next time!')
