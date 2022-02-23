# If the player touches a rock they lose a point.
from services.earn_point import add_point
from game.casting.actor import Actor 
from game.casting.gems_rocks import Rocks

class Lose:
    """Responsible for taking a point away from
    the player when they touch a rock"""
    
    def add(self_.position, Rocks, self_score):
        if  self_.position = Rocks:
            score =+ score - 1 
            if score = 0:
                print('You lose')
            else:
                print('You can do this')
        else:
            score = score 
            
