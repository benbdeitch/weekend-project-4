class Vary:

    def __init__(self, value = None):
        self.value = value

    def get(self):
        return self.value
    
    def set(self, variable):
        self.value = variable