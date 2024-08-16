from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
POSITION = (-210, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.setpos(POSITION)
        self.update_level()


    def update_level(self) -> None:
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(arg=f"Game over. Level: {self.level}", align=ALIGNMENT, font=FONT)
