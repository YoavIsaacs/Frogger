from turtle import Turtle

from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
BOUNDARY_LEFT = 290
BOUNDARY_RIGHT = 280
BOUNDARY_DOWN = -280
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.clear()
        self.setheading(UP)
        self.reset_player()

    def up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def down(self) -> None:
        self.backward(MOVE_DISTANCE)

    def move_left(self) -> None:
        if self.xcor() > -BOUNDARY_LEFT:
            self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self) -> None:
        if self.xcor() < BOUNDARY_RIGHT:
            self.setx(self.xcor() + MOVE_DISTANCE)

    def reset_player(self):
        self.goto(self.xcor(), BOUNDARY_DOWN)

    def did_player_end_level(self, cars: CarManager) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            self.reset_player()
            cars.increment_speed()
            return True
        return False

    def did_player_collide_with_car(self, cars: CarManager) -> bool:
        for car in cars.cars:
            if self.distance(car.pos()) < 20:
                return True
        return False

