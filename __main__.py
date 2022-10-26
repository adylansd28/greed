import os
import random

from pyautogui import position

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 990
ROWS = 45
ELEMENTS = [["rocks","O"], ["gems","*"]]
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 10
MIN_VEL = Point(0,15)
positions = []

for i in range(15,990, 15):
    positions.append(i)


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, CELL_SIZE))
    cast.add_actor("banners", banner)

    # score tracker
    score_tracker = Actor()
    score_tracker.set_text("Score: ")
    score_tracker.set_font_size(FONT_SIZE)
    score_tracker.set_color(WHITE)
    score_tracker.set_position(Point(50,50))
    cast.add_actor("score", score_tracker)

    # create the robot
    x = 450
    y = 585
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    for n in range(DEFAULT_ARTIFACTS):
        random_choice = random.randint(0, 1)
        typeElement = ELEMENTS[random_choice]

        x = random.randint(0, 64)
        y = random.randint(0,3)
        position = Point(positions[x], positions[y])

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_velocity(Point(0,15))
        artifact.set_text(typeElement[1])
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor(typeElement[0], artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()