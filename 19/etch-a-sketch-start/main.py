from turtle import Turtle, Screen
# Example of event listeners
# tim = Turtle()
# screen = Screen()


# def move_forwards():
#     tim.forward(10)


# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()


def main():
    t = Turtle()
    screen = Screen()

    def t_forward():
        t.forward(5)
        
    def t_backward():
        t.backward(5)
    
    def t_left():
        t.left(5)
        
    def t_right():
        t.right(5)

    screen.listen()
    # listen for w to go forward
    screen.onkey(key="w", fun=t_forward)
    # listen for s to go backward
    screen.onkey(key="s", fun=t_backward)
    # listen for a to go counter-clockwise
    screen.onkey(key="a", fun=t_left)
    # listen to d to go clockwise
    screen.onkey(key="d", fun=t_right)
    # listen to c to clear the screen
    screen.onkey(key="c", fun=screen.reset)

    screen.exitonclick()


if __name__ == "__main__":
    main()
