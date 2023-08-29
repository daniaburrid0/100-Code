from turtle import Turtle
from typing import Tuple, List

# Constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_POSITION = (0, 0)
INITIAL_SPEED = 20
SNAKE_COLOR = "white"
SNAKE_SHAPE = "square"

class Snake:
    def __init__(self, num_start: int, first_pos: Tuple[int, int] = INITIAL_POSITION, speed: int = INITIAL_SPEED) -> None:
        """Initialize the Snake with a specified number of starting body parts, initial position, and speed."""
        self.snake_array: List[Turtle] = []
        self.speed: int = speed
        self.first_pos: Tuple[int, int] = first_pos
        for _ in range(num_start):
            self.add_new_body_part()

    def add_new_body_part(self) -> None:
        """Add a new body part to the snake."""
        new_body_part = self.create_body_part()
        if len(self.snake_array) == 0:
            new_body_part.goto(self.first_pos)
        else:
            new_body_part.goto(self.snake_array[-1].position())
        self.snake_array.append(new_body_part)

    def create_body_part(self) -> Turtle:
        """Create and return a new body part."""
        body_part = Turtle(shape=SNAKE_SHAPE)
        body_part.color(SNAKE_COLOR)
        body_part.penup()
        return body_part

    def move(self) -> None:
        """Move the snake forward."""
        for i in range(len(self.snake_array) - 1, 0, -1):
            self.snake_array[i].goto(self.snake_array[i-1].position())
        self.snake_array[0].forward(self.speed)

    def set_heading(self, direction: int) -> None:
        """Set the heading of the snake if it's not opposite to the current heading."""
        if self.snake_array[0].heading() != (direction + 180) % 360:
            self.snake_array[0].setheading(direction)

    def up(self) -> None:
        """Set the heading to UP."""
        self.set_heading(UP)

    def down(self) -> None:
        """Set the heading to DOWN."""
        self.set_heading(DOWN)

    def left(self) -> None:
        """Set the heading to LEFT."""
        self.set_heading(LEFT)

    def right(self) -> None:
        """Set the heading to RIGHT."""
        self.set_heading(RIGHT)
