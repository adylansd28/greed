from game.casting.actor import Actor
from game.shared.point import Point

class Artifact(Actor):

    def __init__(self):
        super().__init__()
        self._message = ""

    def get_color(self):
        """Gets the artifact's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The artifact's text color.
        """
        return super().get_color()

    def get_font_size(self):
        """Gets the artifact's font size.
        
        Returns:
            Point: The artifact's font size.
        """
        return super().get_font_size()

    def get_position(self):
        """Gets the artifact's position in 2d space.
        
        Returns:
            Point: The artifact's position in 2d space.
        """
        return super().get_position()
    
    def get_text(self):
        """Gets the artifact's textual representation.
        
        Returns:
            string: The artifact's textual representation.
        """
        return super().get_text()

    def get_velocity(self):
        """Gets the artifact's speed and direction.
        
        Returns:
            Point: The artifact's speed and direction.
        """
        return super().get_velocity()

    def get_message(self):
        return self._message
    
    def move_next(self, max_x, max_y):
        """Moves the artifact to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity