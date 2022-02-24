# If the player touches a rock they lose a point.
# from services.earn_point import add_point
# from game.casting.actor import Actor 
# from game.casting.gems_rocks import Rocks

class Lose:
    """Responsible for taking a point away from
    the player when they touch a rock"""

    def __init__(self):

        self._position = 0
        self.score = 0
    
    def add(self, Rocks):
        if  self._position == Rocks:
            self.scorescore -= 1 
            if score == 0:
                print('You lose')
            else:
                print('You can do this')
        else:
            score = score 
            
