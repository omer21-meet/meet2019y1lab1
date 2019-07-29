import turtle
turtle.goto(0,0)

turtle.direction = None

def up():
    turtle.direction = 'Up'
    print('You pressed the up key')
    on_move()

turtle.onkey(up, 'Up')
turtle.listen()

def on_move():
    position = turtle.pos()
    if turtle.direction == 'Up':
        turtle.pendown()
        turtle.heading.forward(100)
  
turtle.listen()
