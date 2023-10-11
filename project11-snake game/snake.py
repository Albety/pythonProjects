from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            square = Turtle(shape="square")
            square.color("white")
            square.penup()
            square.goto(pos)
            self.segments.append(square)

    def move(self):
        for pos_segm in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[pos_segm - 1].xcor()
            new_y = self.segments[pos_segm - 1].ycor()
            self.segments[pos_segm].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

