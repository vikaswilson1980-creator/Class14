import turtle
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numsize=6
sidelen=70
angle=360.0 / numsize
for i in range (numsize):
    polygon.forward(sidelen)
    polygon.right(angle)
turtle.done