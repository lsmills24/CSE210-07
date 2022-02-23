# The player (#) can move left or right along the bottom of the screen.
import pyray

class Player:
    """Responsible for the movement of the player
    from left to right on the bottom of the screen"""
    def __init__(self, cell_size = 1):
        self._cell_size = cell_size

    def get_direction(self):

        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1
            
        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction