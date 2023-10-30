import time
from turtle import Screen
from player_turtle import Player
from car_lane import Lane
from start_screen import create_start_screen, hide_start_screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing")
screen.listen()
screen.tracer(0)

create_start_screen()
screen.update()


def start_game():
    hide_start_screen()
    screen.update()
    player = Player()

    game_is_on = True
    game_tick = 0.1

    screen.onkeypress(player.set_movement_up, "w")
    screen.onkeyrelease(player.reset_movement, "w")
    screen.onkeypress(player.set_movement_down, "s")
    screen.onkeyrelease(player.reset_movement, "s")
    screen.onkeypress(player.set_movement_left, "a")
    screen.onkeyrelease(player.reset_movement, "a")
    screen.onkeypress(player.set_movement_right, "d")
    screen.onkeyrelease(player.reset_movement, "d")

    new_lane = Lane()

    def add_car():
        new_lane.create_car()

    screen.onkey(add_car, "q")

    while game_is_on:
        player.player_move()
        new_lane.move_cars()
        time.sleep(game_tick)
        screen.update()


screen.onkey(start_game, "Return")

screen.exitonclick()
