import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("lightgreen")
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.speed("fastest")
        self.goto(random_x, random_y)
        self.refresh
        
    def refresh(self):
        random_x = random.randint(-300, 300)
        random_y = random.randint(-300, 300)
        self.goto(random_x, random_y)