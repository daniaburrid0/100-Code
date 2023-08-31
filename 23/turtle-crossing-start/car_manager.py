from turtle import Turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SHAPE = "square"


class Car(Turtle):
    def __init__(self, shape: str = CAR_SHAPE, undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.goto(300, random.randint(-250, 250))
        self.setheading(180)

    def move(self) -> None:
        self.forward(STARTING_MOVE_DISTANCE)


class CarManager:
    def __init__(self) -> None:
        self.car_list = []

    def create_new_car(self) -> None:
        dice = random.randint(1, 6)
        if dice == 1:
            car = Car()
            self.car_list.append(car)

    def move_cars(self) -> None:
        for car in self.car_list:
            car.move()

    def detect_collision(self, player: Turtle) -> bool:
        for car in self.car_list:
            if car.distance(player) < 20:
                return True
        return False
