from car import Car
import random


class Lane:
    def __init__(self):
        self.y_cor = 0
        self.cars = []
        self.lane_active = True
        self.directions = [-1, 1]
        self.direction = self.directions[random.randint(0, 1)]
        self.lane_activity = 40
        self.car_check = 0

    def create_car(self):
        new_car = Car()
        new_car.goto(320 * -self.direction, self.y_cor)
        self.cars.append(new_car)

    def move_cars(self):
        for _ in self.cars:
            _.goto(_.xcor() + self.direction * _.car_speed, _.ycor())
            if (self.direction == -1 and _.xcor() < -320) or (self.direction == 1 and _.xcor() > 320):
                self.cars.pop(0)
                _.reset()
                _.ht()

    def generate_cars(self):
        self.car_check = random.randint(0, 100)
        if self.car_check < self.lane_activity:
            self.create_car()
