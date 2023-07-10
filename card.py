#This is where it all starts. These objects represent the playing cards. They have a few attributes; name, value, suit, and 'hidden', which is a boolean, and used for showing the displays. 
#Name and Value are generally going to be the same, with the exception of the face cards.  Value is placed as an array, to handle the exception of 

class Card:

    def __init__(self, name, suit):
        self.suit = suit
        self.show = True
        self.name = name
        match name:
            case "2":
                self.value = [2,2]
            case "3":
                self.value = [3,3]
            case "4":
                self.value = [4,4]
            case "5":
                self.value = [5,5]
            case "6":
                self.value = [6,6]
            case "7": 
                self.value = [7,7]
            case "8":
                self.value = [8,8]
            case "9":
                self.value = [9,9]
            case "10":
                self.value = [10,10]
            case "jack":
                self.value = [10,10]
            case "queen":
                self.value = [10,10]
            case "king":
                self.value = [10,10]
            case "ace":
                self.value = [11,1]
        


    def hide(self):
        self.show = False
    def __repr__(self):
        if self.show:
            return f'[{self.name.title()} of {self.suit.title()}]'
        return "[Hidden Card]"
    

    def to_image(self):
        if self.show:
            try:
                value1 = (int(self.name)-1) * 73
            except:
                dict = {"ace":0, "jack": 10, "queen": 11, "king": 12}
                value1 = dict[self.name] *73
        
            dict = {"clubs":0, "spades": 1, "hearts":2, "diamonds": 3}
            value2 = dict[self.suit] * 98
            return [[value1, value2, value1 + 73, value2+98], "images/cards.png"]
        return [[0, 0, 73, 98], "images/card_back.png"]
