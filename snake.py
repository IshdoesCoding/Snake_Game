import turtle
from turtle import Turtle

START_SEGMENT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):

    import turtle

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        global START_SEGMENT
        for segs in START_SEGMENT:
            self.add_segment(segs)

    def move(self):
        global MOVE_DISTANCE
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
        self.head.speed("fastest")

    def add_segment(self, position):
        body_segment = turtle.Turtle("square")
        body_segment.penup()
        body_segment.color("purple")
        body_segment.goto(position)
        self.segments.append(body_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # movement
    def up(self):
         if self.head.heading() != DOWN:
             self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):

        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

