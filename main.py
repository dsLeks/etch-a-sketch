import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def clear():
    t.clear()
    screen.resetscreen()
def forward():
    t.forward(10)

def backward():
    t.backward(10)

def left():
    x = t.heading() - 10
    t.setheading(x)

def right():
    x = t.heading() +10
    t.setheading(x)

screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")
screen.exitonclick()



