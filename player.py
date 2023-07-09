from deck import Deck
from card import Card
from cash_bag import Cash_Bag
class Player: 

    def __init__(self, cash_object, computer = False):
        self.hand = []
        self.cash = cash_object
        self.computer = computer
        self.total = 0
        self.wager = 0
    ##methods:
    #This adds the top card of a deck, or adds an item.. It's meant to be used in the normal gameplay loop
    def hit(self, item):
        if isinstance(item, Deck):
            self.hand.append(item.take_card())
        elif isinstance(item,  Card):
            self.hand.append(item)
        else:
            pass

    def pop_card(self):
        return self.hand.pop()


    ##Cash related methods

    def make_wager(self, bet):
        self.wager += bet
    
    #This method handles 'win'-cases. 
    def pay_out(self):
        self.cash.add(self.wager)
        self.wager = 0

    def lose(self):
        self.cash.subtract(self.wager)
        self.wager = 0
    ###These are the gameplay related methods. 
    def score_hand(self):

#This class is intended to handle the potentiality of splitting hands, by encasing each player inside of an 'array'.




class Over_Player:

    def __init__(self, starting_cash, computer = False):
        self.cash = Cash_Bag(starting_cash)
        player = Player(self.cash, computer)
        self.players = []
        self.players.append(player)

    def check_split(self, player):
        pass



    
