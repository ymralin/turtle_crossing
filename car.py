from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.lane_y = 0
        self.direction = 0
        self.car_speed = 10
        self.pu()
        self.color(colors[random.randint(0, len(colors)-1)])
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.goto(self.xcor()+self.car_speed, self.ycor())
