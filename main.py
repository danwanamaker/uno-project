import deck_functions as df
import hand_functions as hf
import player_functions as pf


class Token:
    def __init__(self):
        self.count = 0
        self.game_over = False
        self.last_card = ''
        self.is_draw_four = False
        self.is_draw_two = False
        self.is_first_reversed = False
        self.is_reversed = False
        self.is_skipped = False
        self.skip_after_draw = self.draw_rules()

    def __str__(self):
        return 'Player ' + str(len(players)) + ': ' + players[self.count].name + ' is up!'

    def increment(self):
        if not self.is_reversed:
            if self.count == len(players) - 1:
                self.count = 0
            else:
                self.count += 1
        else:
            if self.count == 0:
                self.count = len(players) - 1
            else:
                self.count -= 1

    def reverse(self):
        if self.is_reversed:
            self.is_reversed = False
        else:
            self.is_reversed = True

    def draw_rules(self):
        print('House rule: How should drawing work?')
        print('  1. Keep drawing until you get a card you can play')
        print('  2. Draw one card and your turn is over')
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


# SETUP
players = [pf.Player(1, 'Dan'), pf.Player(2, 'Ethan'), pf.Player(3, 'Holton')]  # placeholder players
# players = pf.setup_players()  # actual player constructor
token = Token()
token.last_card = df.choose_card()
while token.last_card[0] == 'w' or token.last_card[1] == 'd' or token.last_card[1] == 's' or token.last_card[1] == 'r':
    df.premade_deck.append(token.last_card)
    token.last_card = df.choose_card()  # So that we don't start the game with a Wild/Skip/Draw/Reverse

# GAMEPLAY LOOP players[token.count] is how we refer to the player whose turn it is.
while not token.game_over:
    if token.is_skipped:  # Program will skip all actions for that player's turn.
        print(players[token.count].name + ', you\'re skipped this turn. Boo hoo, better luck next time!\n')
        token.is_skipped = False  # Clear skip action for next turn.
    else:
        if token.is_first_reversed:  # Give a special greeting to the person right after the reverse.
            print('Back to you, {}!'.format(players[token.count].name))
            token.is_first_reversed = False  # Make it so it doesn't do that again.
        else:
            print('Player {}: {} you\'re up!'.format(token.count + 1, players[token.count].name))
        if token.is_draw_two:
            players[token.count].draw_two()
            token.is_draw_two = False
        elif token.is_draw_four:
            players[token.count].draw_four()
            token.is_draw_four = False
        else:
            players[token.count].holding()
        print('Last card played was a {}.'.format(hf.decode(token.last_card)))

        # ONE PLAYER'S TURN LOOP
        while True:
            print('What would you like to do?')
            print('  1. Draw a card\n  2. Play a card\n--> ', end='')
            prompt = input()
            if prompt == '1':  # Draw a card
                players[token.count].draw_card(read=True)
                players[token.count].holding(now=True)
                if token.skip_after_draw:  # When house rule is active, one card only draw and turn is over.
                    print()
                    break
                print('Last card played was a {}.'.format(hf.decode(token.last_card)))
            elif prompt == '2':  # Play a card
                choice = players[token.count].play_card()
                if choice == -1:  # If they enter 0, this brings them back to the Turn Loop.
                    continue
                chosen_card = players[token.count].hand[choice]  # Retrieve the card from their hand.
                if not hf.is_legal(chosen_card, token.last_card):  # Check that it's a legal play.
                    hf.admonish(chosen_card, token.last_card)
                else:
                    print('You played: ' + hf.decode(chosen_card) + '.')
                    token.last_card = chosen_card  # Store the card that the player played
                    if chosen_card[0] == 'w':  # Record any actions that affect the following player. vv
                        print('What color do you choose?')
                        print('r = Red | y = Yellow | g = Green | b = Blue')
                        wild = input('  --> ')
                        token.last_card = wild + chosen_card[1]
                    if chosen_card[1] == 's':
                        token.is_skipped = True
                    elif chosen_card[1] == 'r':
                        token.reverse()
                        token.is_first_reversed = True
                    elif chosen_card[1] == 'd':
                        token.is_draw_two = True
                    elif chosen_card[1] == 'f':
                        token.is_draw_four = True
                    players[token.count].hand.remove(chosen_card)
                    df.premade_deck.append(chosen_card)  # Discard the played card and return it to the deck.
                    players[token.count].holding(now=True)
                    ending = input('Type "end" to end your turn. --> ')
                    if ending.lower() == 'uno':
                        print(players[token.count].name + ' declares UNO! Watch out!')
                    print()
                    break
            elif prompt == 'done':  # End turn
                break
            elif prompt == 'exit':
                break
    if prompt == 'exit':
        break
    token.increment()
