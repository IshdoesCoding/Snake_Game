from turtle import Turtle
from snake import Snake
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(.90,0.90)
        self.color("red")
        self.speed("fastest")
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x,rand_y)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

