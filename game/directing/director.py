from game.casting.artifact import Artifact
from game.shared.point import Point
import random
from game.shared.color import Color
import time

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.initial_time = time.time()
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        positions = []

        for i in range(15,990, 15):
            positions.append(i)

        robot = cast.get_first_actor("robots")   
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        
        
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        robot.move_next(max_x, max_y)

        banner = cast.get_first_actor("banners")
        score = cast.get_first_actor("score")

        banner.set_text("")

        new_time = time.time()
        time_difference = new_time - self.initial_time

        if time_difference > 0.75:

            self.initial_time = time.time()

            for n in range(5):

                ELEMENTS = [["rocks","O"], ["gems","*"]]

                random_choice = random.randint(0, 1)
                typeElement = ELEMENTS[random_choice]

                x = random.randint(0, 64)
                y = random.randint(0,4)
                position = Point(positions[x], positions[y])

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
                
                artifact = Artifact()
                artifact.set_velocity(Point(0,15))
                artifact.set_text(typeElement[1])
                artifact.set_font_size(15)
                artifact.set_color(color)
                artifact.set_position(position)
                cast.add_actor(typeElement[0], artifact)


        for rock in rocks:
            if robot.get_position().equals(rock.get_position()):
                cast.remove_actor("rocks", rock)
                score.hit_consequence("rock")
                break

        for gem in gems:
            if robot.get_position().equals(gem.get_position()):
                cast.remove_actor("gems", gem)
                score.hit_consequence("gem")
                break

        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        for _rock in rocks:
            _rock.move_next(max_x, max_y)

        for _gem in gems:
            _gem.move_next(max_x, max_y)

        score.set_text(f"Score: {score.get_score()}")

            
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()