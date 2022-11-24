from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.MOVE_DISTANCE = 10

    def move_up(self):
        self.forward(self.MOVE_DISTANCE)

    def end_game(self):
        game = Turtle()
        game.penup()
        game.goto(-30, 0)
        game.write("Game Over", font=("Courier", 14, "normal"))

    def restart(self):
        self.goto(STARTING_POSITION)

    def increase_speed(self):
        self.MOVE_DISTANCE += 5
