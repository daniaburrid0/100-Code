from turtle import Turtle

# Constants
INITIAL_X = 0
INITIAL_Y = 260
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        """Initialize the ScoreBoard class with default shape, undobuffersize, and visibility."""
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(INITIAL_X, INITIAL_Y)
        self.update_display()

    def update_display(self) -> None:
        """Update the score display on the screen."""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)
        
    def increment_score(self) -> None:
        """Increment the score by 1 and update the display."""
        self.score += 1
        self.update_display()

