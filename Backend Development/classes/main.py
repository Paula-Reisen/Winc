# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
from multiprocessing.sharedctypes import Value
from turtle import speed
from webbrowser import get


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        if speed < 0 or speed > 1:
            raise ValueError

    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'

    def strength(self):
        if (self.speed >= self.endurance) and (self.speed >= self.accuracy):
            return ('speed', self.speed)
        if (self.endurance >= self.accuracy):
            return ('endurance', self.endurance)
        else:
            return ('accuracy', self.accuracy)

class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, Player):
        return Player.speed + Player.endurance + Player.accuracy

    def compare_players(self, Player1: Player, Player2: Player, attribute): 
        if getattr(Player1, attribute) > getattr(Player2, attribute):
            return Player1.name
        if getattr(Player2, attribute) > getattr(Player1, attribute):
            return Player2.name
        elif getattr(Player1, attribute) == getattr(Player2, attribute):
            if Player1.strength() > Player2.strength():
                return Player1.name
            if Player2.strength() > Player1.strength():
                return Player2.name
            elif Player1.strength() == Player2.strength():
                if self.sum_player(Player1) > self.sum_player(Player2):
                    return Player1.name
                if self.sum_player(Player2) > self.sum_player(Player1):
                    return Player2.name
                elif self.sum_player(Player1) == self.sum_player(Player2):
                    return 'These two players might as well be twins!'


        