import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('peru')
s.title('Aprendiendo Python 04/02/2023')

t.shapesize(10, 5, 1)
t.shapesize(5, 10, 1)
t.shapesize(3, 3, 3)

t.fillcolor("cyan")
t.forward(100)

t.pencolor('green')
t.forward(100)

t.color("green", "blue")
t.rt(90)
t.forward(100)

t.pensize(5)
t.forward(100)

turtle.done()