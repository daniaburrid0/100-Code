from turtle import Turtle

# Constants
FONT: tuple = ("Courier", 24, "normal")
COLOR: str = "black"
POSITION: tuple = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color(COLOR)
        self.goto(POSITION)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
