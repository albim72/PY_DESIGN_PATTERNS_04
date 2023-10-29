from pyparsing import Word,OneOrMore,Optional,Group,Suppress,alphanums

class Gate:
    def __init__(self):
        self.is_open = False
        
    def __str__(self):
        return 'open' if self.is_open else 'closed'
    
    def open(self):
        print('opening the gate')
        self.is_open = True
        
    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False
