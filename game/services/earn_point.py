# If the player touches a gem they earn a point.
# from game.casting.gems_rocks import Gem
# from game.casting.actor import Actor
class AddPoint: 
    self_score = 0 

    def __init__(self):

        self._position = 0
        self.score = 0

    def add(self):
        self.score += 1 
        
            