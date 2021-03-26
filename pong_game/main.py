import turtle
from Paddle import Paddle
from Ball import Ball

WIN = turtle.Screen() #the screen
WIN.title("Pong game")
WIN.bgcolor("black")
WIN.setup(width=800, height = 600)
WIN.tracer(0) #stops the window from updating
    
#objects
paddle1 = Paddle("green",-350,0)
paddle2 = Paddle("red", 350,0)
ball = Ball("orange",1)

while True:
    WIN.update()