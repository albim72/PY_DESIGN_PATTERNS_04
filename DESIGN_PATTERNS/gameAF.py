#defnicja FrogGame

class Frog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self,obstacle):
        act = obstacle.action()
        msg = f'Żaba {self} spotyka {obstacle} i {act}!'
        print(msg)

class Bug:
    def __str__(self):
        return 'robak'

    def action(self):
        return 'zjada go'

class FrogWorld:
    def __init__(self,name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----------- FROG WORLD ------------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


#defnicja WarlockGame

class WarLock:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self,obstacle):
        act = obstacle.action()
        msg = f'Czarnoksiążnik {self} spotyka {obstacle} i {act}!'
        print(msg)

class Ork:
    def __str__(self):
        return 'orka'

    def action(self):
        return 'zabija go'

class WarLockWorld:
    def __init__(self,name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----------- WARLOCK WORLD ------------'

    def make_character(self):
        return WarLock(self.player_name)

    def make_obstacle(self):
        return Ork()


#Środowisko gry

class GameEnvironment:
    def __init__(self,factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
        
    def play(self):
        self.hero.interact_with(self.obstacle)

