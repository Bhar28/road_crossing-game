from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.write(f"Level: {self.level}", font=("Courier", 12, "normal"))

    def show_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=("Courier", 12, "normal"))