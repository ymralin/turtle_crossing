from turtle import Turtle
import random

start_screen = []
colors = ["red", "orange", "green", "blue", "indigo", "violet"]
current_color = colors[random.randint(0, len(colors) - 1)]


def create_start_screen():
    title = Turtle()
    title.pu()
    title.ht()
    title.color(current_color)
    title.goto(0, 100)
    title.write("Turtle crossing", align="center", font=("Arial", 48, "normal"))
    start_screen.append(title)

    press_start = Turtle()
    press_start.pu()
    press_start.ht()
    press_start.color(current_color)
    press_start.goto(0, 00)
    press_start.write("Press Enter to start game", align="center", font=("Arial", 24, "normal"))
    start_screen.append(press_start)

    controls = Turtle()
    controls.pu()
    controls.ht()
    controls.color(current_color)
    controls.goto(0, -80)
    controls.write("Controls: W, S, A, D", align="center", font=("Arial", 18, "normal"))
    start_screen.append(controls)


def hide_start_screen():
    for _ in start_screen:
        _.clear()
