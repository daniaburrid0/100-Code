from turtle import Turtle

# constants
FONT = ('Courier', 80, 'normal')
ALIGNMENT = 'center'
X_POSITION = 0
Y_POSITION = 200
COLOR = 'white'

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color(COLOR)
        self.penup()
        self.goto(X_POSITION, Y_POSITION)
        self.player1_score = 0
        self.player2_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self) -> None:
        """Update the scoreboard."""
        self.clear()
        self.write(f"{self.player1_score} : {self.player2_score}", align=ALIGNMENT, font=FONT)
        
    def increase_player1_score(self) -> None:
        """Increase the player1 score."""
        self.player1_score += 1
        self.update_scoreboard()
    
    def increase_player2_score(self) -> None:
        """Increase the player2 score."""
        self.player2_score += 1
        self.update_scoreboard()