#This class exists for one main purpose; when splitting hands, it will be annoying to link the duplicate player's hands together, if they are not tied to the same object. 


class Cash_Bag:
    
    def __init__(self, cash_value):
        self.value = cash_value
        

    #This method allows altering the wager, without having to directly edit the variable. 
    def add(self,cash):
        self.value += cash
    
    def subtract(self, cash):
        self -= cash
    
    def get(self):
        return self.value