from card import Card
from deck import Deck
import window
from vary import Vary
from player import Player


player_number = ""
bet_value = ""
starting_cash = ""
vary = Vary()


run = window.Intro(vary)

if not vary.get():
    quit()

vary.set(5)
run = window.Game_Window(vary)
