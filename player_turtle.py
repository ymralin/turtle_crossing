from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.setheading(90)
        self.shape("turtle")
        self.color("red")
        self.goto(0,-280)

    step = 20
    # movement direction 1,2,3,4 = right, up, left, down
    movement = 0

    def set_movement_right(self):
        self.movement = 1

    def set_movement_up(self):
        self.movement = 2

    def set_movement_left(self):
        self.movement = 3

    def set_movement_down(self):
        self.movement = 4

    def reset_movement(self):
        self.movement = 0

    def player_move(self):
        new_x = self.xcor()
        new_y = self.ycor()
        if self.movement == 1:
            new_x += self.step
        elif self.movement == 2:
            new_y += self.step
        elif self.movement == 3:
            new_x -= self.step
        elif self.movement == 4:
            new_y -= self.step
        self.goto(new_x, new_y)
