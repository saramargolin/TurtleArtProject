import turtle
bob = turtle.Turtle()
bob.width(3)
bob.speed(100)
turtle.colormode(255)
turtle.bgcolor("black")

for times in range(234):
    c = (0, 206, 209)
    bob.color(c)
    bob.circle(255-times)
    bob.right(135)
for times in range(150):
    c = (0,0,0)
    bob.color(c)
    bob.circle(125-times)
    bob.right(135)
for times in range(50):
    c = (234,254,112)
    bob.color(c)
    bob.circle(175-times)
    bob.right(135)
turtle.done()
