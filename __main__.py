#Imports
import random

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.directing.director import Director

from game.casting.cast import Cast
from game.casting.artifact import Artifact
from game.casting.actor import Actor

from game.shared.color import Color
from game.shared.point import Point

#Constants
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DEFAULT_PIECES = 100
WHITE = Color(255, 255, 255)

messages = ['Gem','Rock','Gem','Rock','Gem','Rock','Gem','Rock']
pieces = ['*','o','*','o','*','o','*','o']

def main():
    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - 25) #lower part of screen
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    for n in range(DEFAULT_PIECES):
        ranNum = random.randrange(0,7)
        text = pieces[ranNum]
        message = messages[ranNum]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        #Move 5 each cycle
        artifact.set_velocity(Point(0,5))
        cast.add_actor("artifacts", artifact)
    
    #Start of Game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()