from turtle import Turtle, Screen
import random


def main():
    # make the screen and set it up 500x400
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.colormode(255)

    # make 4 turtles and set their colors like the ninja turtles
    colors = ["red", "blue", "orange", "purple"]
    turtle = [Turtle(shape="turtle") for _ in range(4)]

    # set the turtles up in their starting positions
    for i in range(4):
        turtle[i].color(colors[i])
        turtle[i].penup()
        turtle[i].goto(x=-230, y=-100 + i * 50)

    user_bet = screen.textinput(title="$", prompt="Who do you think will win?")

    if user_bet:
        loop = True
        while loop:
            for i in range(4):
                turtle[i].forward(random.randint(0, 10))
                if turtle[i].xcor() >= 230.00:
                    loop = False
                    if user_bet == turtle[i].pencolor():
                        print(
                            f"You won! The {turtle[i].pencolor()} turtle won!")
                    else:
                        print(
                            f"You lost! The {turtle[i].pencolor()} turtle won!")
                    break


if __name__ == "__main__":
    main()
