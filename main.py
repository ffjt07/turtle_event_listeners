from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()

def move_forward():
   turt.forward(15)

def move_backward():
   turt.backward(15)

def turn_counter_clockwise():
   turt.left(15)

def turn_clockwise():
   turt.right(15)

def clear_screen():
   turt.home()
   turt.clear()
   

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()