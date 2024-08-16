import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main() -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    cars: CarManager = CarManager()
    player: Player = Player()
    scoreboard: Scoreboard = Scoreboard()


    screen.listen()

    check = 0

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        screen.onkeypress(fun=player.up, key="Up")
        screen.onkeypress(fun=player.down, key="Down")
        screen.onkeypress(fun=player.move_right, key="Right")
        screen.onkeypress(fun=player.move_left, key="Left")
        if player.did_player_collide_with_car(cars):
            game_is_on = False
            scoreboard.game_over()
        else:
            if player.did_player_end_level(cars):
                scoreboard.update_level()


        cars.create_new_car()
        cars.move_cars()


    screen.exitonclick()

if __name__ == '__main__':
    main()
