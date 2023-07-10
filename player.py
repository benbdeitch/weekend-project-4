from deck import Deck
from card import Card
from cash_bag import Cash_Bag
class Player: 

    def __init__(self, cash, computer = False):
        self.hand = []
        self.cash = Cash_Bag(cash)
        self.computer = computer
        
        self.wager = 0
    ##methods:
    #This adds the top card of a deck, or adds an item.. It's meant to be used in the normal gameplay loop
    def hit(self, item):
        if isinstance(item, Deck):
            value = item.take_card()
        elif isinstance(item,  Card):
            value = item
        else:
            value = None
        if isinstance(value,Card):
            if value.name == "ace":
                self.hand.append(value)
            else:
                self.hand.insert(0, value)
    def pop_card(self):
        return self.hand.pop()


    ##Cash related methods
    def get_cash(self):
        return self.cash.get()
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
        total = 0
        for cards in self.hand:
            if total+ cards.value[0]  < 22:
                total+= cards.value[0]
            elif total + cards.value[1] < 22:
                total += cards.value[1]
            else:
                total = -1
                break
        if total == 21 and len(self.hand) == 2:
            return 100
        
        return total




    