from turtle import Turtle

STARTING_LOCATIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.snakeParts = []
        self.create_snake()
        self.head = self.snakeParts[0]
    
    def create_snake(self):
        for location in STARTING_LOCATIONS:
            self.add_segment(location)
    
    def add_segment(self, location):
        snake = Turtle("square")
        snake.color("#fff")
        snake.up()
        snake.setpos(location)
        self.snakeParts.append(snake)
    
    def increase_snake_length(self):
        new_x = self.snakeParts[-1].xcor()
        new_y = self.snakeParts[-1].ycor()
        self.add_segment((new_x, new_y))
    
    def move(self):
        for index in range(len(self.snakeParts)-1, 0, -1):
            new_x = self.snakeParts[index-1].xcor()
            new_y = self.snakeParts[index-1].ycor()
            self.snakeParts[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def to_top(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def to_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def to_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def to_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
