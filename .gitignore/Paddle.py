import turtle

class Paddle (turtle.Turtle):
    def __init__(self, color,x,y):
        self._position = (x,y)
        self = turtle.Turtle()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y)
        


        

    

