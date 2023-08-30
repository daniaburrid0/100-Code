from turtle import Turtle

# constants
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 20
X_POSITION_RIGHT = 350
Y_POSITION_RIGHT = 0
X_POSITION_LEFT = -350
Y_POSITION_LEFT = 0
PADDLE_COLOR = 'white'
PADDLE_SHAPE = 'square'
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600


class Paddle(Turtle):
    def __init__(self, shape: str = PADDLE_SHAPE, undobuffersize: int = 1000, visible: bool = True, player: int = 1) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_wid=PADDLE_HEIGHT / 20,
                       stretch_len=PADDLE_WIDTH / 20)
        self.color(PADDLE_COLOR)
        if player == 1:
            self.setpos(X_POSITION_RIGHT, Y_POSITION_RIGHT)
        else:
            self.setpos(X_POSITION_LEFT, Y_POSITION_LEFT)
    
    def up(self) -> None:
        """Move the paddle up if not at the top of the screen."""
        if self.ycor() < SCREEN_HIGHT / 2 - PADDLE_HEIGHT / 2:
            self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)
    
    def down(self) -> None:
        """Move the paddle down if not at the bottom of the screen."""
        if self.ycor() > -SCREEN_HIGHT / 2 + PADDLE_HEIGHT / 2:
            self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)