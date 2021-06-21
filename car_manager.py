from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_array = []
    
    def create_car(self):
        new_car = Turtle("square")
        new_car.color(COLORS[random.randint(0, len(COLORS) - 1)])
        new_car.penup()
        new_car.shapesize(1, 2, 1)
        new_car.goto(x = 300, y = random.randint(-250, 250))
        self.cars_array.append(new_car)

    def move_cars(self):
        for car in self.cars_array:
            car.setx(car.xcor() - MOVE_INCREMENT )