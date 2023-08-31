from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard
from typing import *

# Constants
SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600
SNAKE_COLLISION_DISTANCE: int = 10
FOOD_COLLISION_DISTANCE: int = 15
WALL_LIMIT: int = 280
SLEEP_INTERVAL: int = 0.2

def setup_screen() -> Screen:
    """Setup and return the turtle screen."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen

def setup_event_handling(screen: Screen, snake: Snake) -> None:
    """Set up key event handling for the snake's movement."""
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

def check_collision_with_food(snake: Snake, food: Food, score: ScoreBoard) -> None:
    """Check for collision between snake and food, update score and snake length accordingly."""
    if snake.snake_array[0].distance(food) < FOOD_COLLISION_DISTANCE:
        food.refresh_position()
        score.increment_score()
        snake.add_new_body_part()

def check_collision_with_body(snake: Snake, score: ScoreBoard) -> bool:
    """Check for collision between the snake's head and body, return True if collided."""
    for body_part in snake.snake_array[1:]:
        if snake.snake_array[0].distance(body_part) < SNAKE_COLLISION_DISTANCE:
            print(f"Game Over - Hit the body - Score: {score.score}")
            return True
    return False

def check_collision_with_wall(snake: Snake, score: ScoreBoard) -> bool:
    """Check for collision with the wall, return True if collided."""
    head = snake.snake_array[0]
    if abs(head.xcor()) > WALL_LIMIT or abs(head.ycor()) > WALL_LIMIT:
        print(f"Game Over - Hit the wall - Score: {score.score}")
        return True
    return False

def start_game(snake: Snake, food: Food, screen: Screen) -> None:
    """Main game loop."""
    score = ScoreBoard()
    while True:
        sleep(SLEEP_INTERVAL)
        screen.update()
        snake.move()
            
        check_collision_with_food(snake, food, score)
        
        if check_collision_with_body(snake, score) or check_collision_with_wall(snake, score):
            score.reset_score()
            snake.start_egain()

def main():
    screen = setup_screen()
    snake = Snake(3)
    food = Food()
    screen.update()

    setup_event_handling(screen, snake)
    
    start_game(snake, food, screen)

if __name__ == "__main__":
    main()
