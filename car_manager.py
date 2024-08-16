import random
from turtle import Turtle
from typing import Tuple

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_STRETCH = 2
BOUNDARY = 280
LEFT = 180


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()


    def create_car(self) -> None:
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=CAR_STRETCH)
        car.color(random.choice(COLOURS))
        car.penup()
        car.goto(self.create_random_position())
        car.setheading(LEFT)
        car.speed = self.cars_speed
        self.cars.append(car)


    def move_cars(self) -> None:
        for car in self.cars:
            car.forward(self.cars_speed)

    def increment_speed(self) -> None:
        self.cars_speed += MOVE_INCREMENT

    def create_new_car(self) -> None:
        should_create = random.randint(0, 3)
        if should_create == 0:
            self.create_car()

    def delete_cars(self):
        for car in self.cars:
            if car.ycor() > 320:
                del car


    @staticmethod
    def create_random_position() -> Tuple[int, int]:
        y = random.randint(-BOUNDARY, BOUNDARY)
        return 300, y
