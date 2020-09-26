import turtle

turtle.up()
turtle.goto(-40, 0)
turtle.down()


def shape_sqare():
    turtle.pensize(2)
    i=0
    turtle.left(50)
    while i<4:
        turtle.forward(160)
        turtle.left(90)
        i+=1
    turtle.up()
    turtle.right(50)

def shape_circle():
    turtle.pensize(5)
    turtle.goto(-50, -50)
    turtle.down()
    turtle.circle(160, 360)
    turtle.up()

def shape_hexagon():
    turtle.pensize(7)
    i=0
    turtle.goto(50, -100)
    turtle.down()
    while i<6:
        turtle.left(360/6)
        turtle.fd(1420/6)
        i+=1
    turtle.up()


shape_sqare()
shape_circle()
shape_hexagon()
turtle.done()