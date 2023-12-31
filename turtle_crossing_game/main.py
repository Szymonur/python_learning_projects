import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.onkey(player.move, "Up")

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.append_cars()
    car_manager.check_colison(player.position())
    screen.update()
