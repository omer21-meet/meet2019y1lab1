import turtle
turtle.bgcolor('lightblue')
turtle.penup()
turtle.color('yellow')
turtle.pencolor('yellow')
turtle.goto(-600,400)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.right(70)
turtle.pensize(20)
print(turtle.pos())
turtle.forward(100)
turtle.goto(-600,400)
turtle.left(110)
turtle.forward(120)
turtle.right(70)
turtle.forward(100)
turtle.mainloop()
