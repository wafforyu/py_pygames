import turtle

class Ball(turtle.Turtle):
    def __init__(self,color,speed):
        self = turtle.Turtle()
        self.speed(speed)
        self.shape("circle")
        self.color(color)
        self.penup()
        self.goto(0,0)