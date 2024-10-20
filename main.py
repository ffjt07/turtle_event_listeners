from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forward():
   turt.forward(10)

screen.listen()
screen.onkey(move_forward, "space")
screen.exitonclick()