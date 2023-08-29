from turtle import Turtle
import random

# Constants
MIN_X = -280
MAX_X = 280
MIN_Y = -280
MAX_Y = 280

class Food(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        """Initialize the Food class with default shape, undobuffersize, and visibility status."""
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_position()

    def random_coordinate(self, min_val: int, max_val: int) -> int:
        """Generate a random coordinate within the given min and max range."""
        return random.randint(min_val, max_val)

    def refresh_position(self) -> None:
        """Refresh the position of the food on the screen."""
        random_x = self.random_coordinate(MIN_X, MAX_X)
        random_y = self.random_coordinate(MIN_Y, MAX_Y)
        self.goto(random_x, random_y)

