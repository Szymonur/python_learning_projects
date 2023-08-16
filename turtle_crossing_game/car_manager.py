import time
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.append_cars()
        self.hideturtle()

    def append_cars(self):
        number_of_cars = random.randint(0, 2)
        for _ in range(number_of_cars):
            position = (360,  random.randint(-250, 280))
            car = Car(position)
            self.cars.append(car)
        self.move_cars()
        time.sleep(0.4)

    def move_cars(self):
        for _ in range(random.randint(3, 5)):
            for car in self.cars:
                if car.xcor() <= -320:
                    self.cars.remove(car)
                car.forward(10)

    def check_colison(self, car_position):
        for car in self.cars:
            if car.distance(car_position) < 30:
                print("game over!")


class Car(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.pu()
        self.goto(position)
        self.speed("slowest")

