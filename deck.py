#This is the deck object. Primarily, it is used as an array of cards, and as the primarily means of accessing them. 
from card import Card
from random import shuffle
class Deck:


    def __init__(self, number):
        self.cards = []
        
        cards = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        suits = ["hearts", "spades", "clubs", "diamonds"]

        for value in cards:
            for suit in suits:
                for iter in range(number):
                    self.cards.append( Card(value, suit))
        self.shuffle()
    
    def shuffle(self):
        shuffle(self.cards)
    
    #Adds cards back in:
    def add_cards(self, *args):
        for arg in args:
            if isinstance(arg, Card):
                self.card.append(arg)
        self.shuffle()

    #Removes the top card:
    def take_card(self): 
        return self.cards.pop()
    
    def take_card_hide(self):
        card =self.cards.pop()
        card.hide()
        return card
    
    def __repr__(self):
        string= []
        for x in self.cards:
            string.append(repr(x))
        return ", ".join(string)

         