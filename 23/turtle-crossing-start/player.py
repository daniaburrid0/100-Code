from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
SHAPE = "turtle"
COLOR = "black"


class Player(Turtle):
    def __init__(self, shape: str = SHAPE, undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color(COLOR)
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def move_down(self) -> None:
        self.backward(MOVE_DISTANCE)

    def move_left(self) -> None:
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self) -> None:
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def is_at_finish_line(self) -> bool:
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self) -> None:
        self.goto(STARTING_POSITION)
