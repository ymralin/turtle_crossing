from car import Car
import random


class Lane:
    def __init__(self):
        self.y_cor = 0
        self.cars = []
        self.lane_active = True
        self.directions = [-1, 1]
        self.direction = self.directions[random.randint(0, 1)]

    def create_car(self):
        new_car = Car()
        new_car.goto(320 * -self.direction, 0)
        self.cars.append(new_car)

    def move_cars(self):
        for _ in self.cars:
            _.goto(_.xcor() + self.direction * _.car_speed, _.ycor())
