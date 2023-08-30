from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SLEEP_TIME = 0.1


def setup_screen() -> Screen:
    """Setup the screen for the game."""
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor('black')
    screen.title('Pong')
    screen.tracer(0)
    return screen


def setup_event_handling(screen: Screen, paddle: Paddle, up_key: str, down_key: str) -> None:
    """Configure event handlers for a paddle."""
    screen.listen()
    screen.onkeypress(paddle.up, up_key)
    screen.onkeypress(paddle.down, down_key)

def detect_collision(ball: Ball, p1: Paddle, p2: Paddle) -> None:
    """Detect collision between the ball and the wall or the paddles."""
    # TODO: put this function in the Ball class
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.distance(p1) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.acelerate()
    elif ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.acelerate()
    
def detect_goal(ball: Ball, score: Scoreboard) -> None:
    """Detect if a goal is scored."""
    if ball.xcor() > 380:
        ball.reset_position(1)
        score.increase_player2_score()
    elif ball.xcor() < -380:
        ball.reset_position(2)
        score.increase_player1_score()
    else:
        return 0


def main():
    """Main function."""
    screen = setup_screen()
    player1 = Paddle(player=1)
    player2 = Paddle(player=2)
    score = Scoreboard()
    ball = Ball()
    ball.start_moving()
    
    setup_event_handling(screen, player2, 'w', 's')
    setup_event_handling(screen, player1, 'Up', 'Down')
    
    game_is_on = True
    while game_is_on:
        time.sleep(SLEEP_TIME/ball.aceleration)
        ball.move()
        detect_collision(ball, player1, player2)
        detect_goal(ball, score)
        screen.update()


if __name__ == '__main__':
    main()
