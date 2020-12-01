from tkinter import *
from tkinter import simpledialog

import hand_functions as hf
import player_functions as pf


players = [pf.Player(1, 'Dan'), pf.Player(2, 'Ethan'), pf.Player(3, 'Holton')]  # placeholder players


class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.window = Frame(parent)
        self.window.pack()

        self.players_list = []
        for player in players:
            label_string = 'Player {}: {} '.format(player.number, player.name)
            label_string += '🃏'*len(player.hand)
            player_label = Label(self.window, text=label_string)
            player_label.pack()
        for card in players[0].hand:
            color = hf.decode_color(card).lower()
            if color == '':  # This is because the function returns '' if it receives a Wild card
                color = 'white'  # And I want that to be white
            card_text = hf.decode(card)
            card_button = Button(self.window, bg=color, text=card_text)
            card_button.pack(side=LEFT)
        self.my_string = StringVar()
        self.my_label = Label(self.window, text='Enter name: ')
        self.my_label.pack(side=LEFT)
        self.my_entry = Entry(self.window, textvariable=self.my_string)
        self.my_entry.pack(side=LEFT)

        self.enter_key = Button(self.window, text='Enter', command=self.get_value)
        self.enter_key.pack(side=LEFT)

        my_name = simpledialog.askstring('Enter name', 'Enter name (or enter "done" if all players are entered):')
        print(my_name)

    def get_value(self):
        self.my_string = self.my_entry.get()
        print(self.my_string)


root = Tk()
my_app = MyApp(root)
root.mainloop()
