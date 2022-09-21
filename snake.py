from turtle import Turtle, left, right, setheading, up
import random
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
COLOR_LIST = [
	(0, 255, 255),
	(127, 255, 212),
	(118, 238, 198),
	(102, 205, 170),
	(69, 139, 116),
	(227, 207, 87),
	(0, 0, 255),
	(0, 0, 238),
	(0, 0, 205),
	(0, 0, 139),
	(138, 43, 226),
	(255, 64, 64),
	(238, 59, 59),
	(152, 245, 255),
	(142, 229, 238),
	(255, 97, 3),
    (255, 153, 18),
	(127, 255, 0),
	(118, 238, 0),
	(102, 205, 0),
	(69, 139, 0),
	(61, 89, 171),
	(61, 145, 64),
	(255, 127, 80),
	(100, 149, 237),
	(220, 20, 60),
	(0, 238, 238),
	(0, 205, 205),
	(255, 185, 15),
	(238, 173, 14),
	(202, 255, 112),
	(188, 238, 104),
	(162, 205, 90),
	(191, 62, 255),
	(154, 50, 205),
	(104, 34, 139),
    (233, 150, 122),
	(193, 255, 193),
	(180, 238, 180),
	(151, 255, 255),
	(141, 238, 238),
	(148, 0, 211),
	(255, 20, 147),
	(238, 18, 137),
	(205, 16, 118),
	(139, 10, 80),
	(0, 191, 255),
	(0, 154, 205),
	(0, 104, 139),
	(30, 144, 255),
	(28, 134, 238),
	(24, 116, 205),
	(16, 78, 139),
	(252, 230, 201),
	(0, 201, 87),
	(178, 34, 34),
	(255, 48, 48),
	(205, 38, 38),
	(255, 125, 64),
	(34, 139, 34),
	(255, 215, 0),
	(238, 201, 0),
	(255, 193, 37),
	(238, 180, 34),
	(205, 155, 29),
	(139, 105, 20)
]
MOVE_DISTANCE = 20
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
        for position in STARTING_POSITIONS:   
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        random_color = random.choice(COLOR_LIST)
        new_segment.color(random_color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)