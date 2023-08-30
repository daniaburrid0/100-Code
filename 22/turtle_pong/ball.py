from turtle import Turtle

# constants
BALL_SPEED = 10
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_SHAPE = 'circle'
BALL_COLOR = 'white'
X_STARTING_POSITION = 0
Y_STARTING_POSITION = 0

class Ball(Turtle):
    def __init__(self, shape: str = BALL_SHAPE, undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color(BALL_COLOR)
        self.penup()
        self.shapesize(stretch_wid=BALL_WIDTH/20, stretch_len=BALL_HEIGHT/20)
        self.startin_position()
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.aceleration = 1
        
    def startin_position(self) -> None:
        """Set the starting position of the ball."""
        self.goto(X_STARTING_POSITION, Y_STARTING_POSITION)
        self.aceleration = 1
    
    def start_moving(self) -> None:
        """Start moving the ball."""
        self.setheading(45)
        self.move()
    
    def move(self) -> None:
        """Move the ball."""
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self) -> None:
        """Bounce the ball."""
        self.y_move *= -1
    
    def bounce_x(self) -> None:
        """Bounce the ball."""
        self.x_move *= -1
    
    def acelerate(self) -> None:
        """Acelerate the ball."""
        self.aceleration += 0.2
    
    def reset_position(self, player_win: int) -> None:
        """Reset the position of the ball."""
        if player_win == 1:
            self.startin_position()
            self.bounce_x()
        else:
            self.startin_position()
            self.bounce_x()