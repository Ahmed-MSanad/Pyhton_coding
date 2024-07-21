from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.5, 0.5)
        self.color("#09c")
        self.speed("fastest")
        self.up()
        self.set_food()
    
    def set_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)
