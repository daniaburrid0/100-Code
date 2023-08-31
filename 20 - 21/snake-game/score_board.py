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
        self.high_score = 0
        self.load_high_score()
        self.update_display()
        
    def load_high_score(self) -> None:
        """Load the high score from the file if exists if not create one."""
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("high_score.txt", "w") as file:
                file.write("0")
    
    def update_high_score(self) -> None:
        """Update the high score in the file deleting the previous one."""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def update_display(self) -> None:
        """Update the score display on the screen."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)
        
    def increment_score(self) -> None:
        """Increment the score by 1 and update the display."""
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.update_display()
    
    def reset_score(self) -> None:
        self.score = 0
        self.update_display()

