from turtle import Turtle, Screen, register_shape, mainloop
from PIL import Image
import pandas as pd

# Constants
COLOR = "black"


def get_width_height(image_path: str) -> tuple:
    """Returns the width and height of an image."""
    image = Image.open(image_path)
    width, height = image.size
    return width, height


def screen_setup(width: int, height: int, background_image_path: str) -> Screen:
    """Sets up the turtle screen with a background image."""
    register_shape(background_image_path)
    screen = Screen()
    screen.bgpic(background_image_path)
    screen.setup(width=width, height=height)
    return screen


class State(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color(COLOR)

    def set_state(self, state: str, x_cor: int, y_cor: int) -> None:
        """Sets the turtle to a state location and writes the state name."""
        self.goto(x_cor, y_cor)
        self.write(state, align="center", font=("Arial", 8, "normal"))


def main() -> None:
    width, height = get_width_height("blank_states_img.gif")
    screen = screen_setup(width, height, "blank_states_img.gif")
    states_df = pd.read_csv("50_states.csv")
    score = states_df.shape[0]
    while score > 0:
        answer_state = screen.textinput(
            title=f"{score} States Correct", prompt="What's another state's name?").title()
        if answer_state == "Exit":
            break
        if answer_state in states_df.values:
            state = State()
            state.set_state(answer_state, 
                            int(states_df.loc[states_df["state"] == answer_state, "x"].iloc[0]), 
                            int(states_df.loc[states_df["state"] == answer_state, "y"].iloc[0]))
            score -= 1
    mainloop()


if __name__ == "__main__":
    main()
