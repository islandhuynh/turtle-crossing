import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
SPEED_INCREASE = 0.9

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing by Island Huynh")
player_icon = Player()
level = Scoreboard()
cars = CarManager()

screen.onkeypress(player_icon.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    random_int = random.randint(1, 5)
    if random_int == 5:
        cars.create_car()
    cars.move_cars()
    time.sleep(0.15 * (0.9**level.score))
    screen.update()
    if player_icon.ycor() > FINISH_LINE_Y:
        player_icon.reset()
        level.increase_Score()
    for car in cars.cars_array:
        if player_icon.distance(car) < 25:
            level.game_over()
            game_is_on = False

screen.exitonclick()