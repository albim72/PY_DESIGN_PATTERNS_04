class Musician:
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        return f'Musician {self.name}'
    
    def play(self):
        return "play the music!"


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Dancer {self.name}'

    def play(self):
        return "dance!"
