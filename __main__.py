import random

from game.casting.gems_rocks import Gem
from game.casting.gems_rocks import Rocks
from game.casting.removed import Removed 

from game.directing.director import Director

from game.services.earn_point import Point
from game.services.lose_point import Lose
from game.services.player_move import Player

from game.shared.color import Color

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Gems and Rocks"
# DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

def main():
    """main"""
    for n in range(Gem, Rocks):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        gem.set_color(color)
        rock.set_color(color)
        gem.set_position(position)
        rock.set_position(position)
        
    


director = Director(Player)
director.start_game(Director)


if __name__ == "__main__":
    main()
