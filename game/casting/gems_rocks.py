# Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
# from game.shared.color import Color
from game.casting.actor import Actor

class Gem(Actor):
    """Responsible for random Gems appearing at the top
    and falling down.
    This class will pull from color.py for the random colors"""
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the gem's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message




class Rocks(Actor):
    """Responsible for random rocks appearing at the top
    and falling down"""
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the rock's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message    
        
        
        
#drop down from top goes here
class drop_down(Actor):
