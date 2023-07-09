from card import Card
from deck import Deck 
from game_table import Table
import window
from vary import Vary



player_number = ""
bet_value = ""
starting_cash = ""
vary = Vary()


run = window.Intro(vary)

if not vary.get():
    quit()

run = window.Starter(vary)