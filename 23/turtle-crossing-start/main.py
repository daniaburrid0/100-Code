import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Constants
SCREEN_WHIDTH: int = 600
SCREEN_HEIGHT: int = 600


def screen_setup() -> Screen:
    screen = Screen()
    screen.setup(width=SCREEN_WHIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    return screen


def event_handler(screen: Screen, player: Player) -> None:
    screen.listen()
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")


def main():
    screen = screen_setup()
    player = Player()
    score = Scoreboard()
    event_handler(screen, player)
    car_manager = CarManager()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        car_manager.create_new_car()
        car_manager.move_cars()
        if car_manager.detect_collision(player):
            score.game_over()
            game_is_on = False
        if player.is_at_finish_line():
            player.go_to_start()
            score.increase_score()
        screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
