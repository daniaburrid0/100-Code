import colorgram
from turtle import *
import random

def extract_rgb_colors():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    rgb_colors = rgb_colors[2:]
    return rgb_colors

def draw_line_of_dots(t, screen_size, size=20, color=[]):
    line_length = screen_size - 100
    total_dots = len(color)
    space_between_dots = int(line_length / total_dots)
    for _ in range(total_dots):
        t.dot(size, random.choice(color))
        t.forward(space_between_dots)
    t.dot(size, random.choice(color))

def move_to_next_line(t, screen_size, direction):
    t.left(direction * 90)
    t.forward(int(screen_size/20))
    t.left(direction * 90)

def main():
    colors = extract_rgb_colors()
    t = Turtle()
    screen = Screen()
    screen.colormode(255)
    size = min(screen.window_width(), screen.window_height()) - 25
    t.penup()
    t.goto(-size/2, -size/2)
    t.penup()
    t.speed("fastest")

    direction = 1
    for _ in range(10):
        draw_line_of_dots(t, size, 15, colors)
        move_to_next_line(t, size, direction)
        direction *= -1

    t.hideturtle()
    done()
    
if __name__ == "__main__":
    main()
