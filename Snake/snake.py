import turtle
import random
turtle.bgcolor('green')
turtle.tracer(1,0)

SIZE_X = 800
SIZE_Y = 500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 8
TIME_STEP = 100

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")
snake.pensize(30)

turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()
    pos_list.appned(pos_list)
    pos_list=snake.stamp()
    pos_list.appned(stamp_list)
    
for piece in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE
    snake.goto(x_pos,y_pos)
    snake.pendown()

def remove_tail():
    old_stamp= stamp_list(0)
    snake.clearstamp(old_stamp)
    pop_list.pop(0)
    
snake.direction = 'Up'
def up():
    snake.directrion = 'Up'
    move_snake()
    print("You pressed the up key!")

snake.direction = 'Down'
def down():
    snake.directrion = 'Down'
    move_snake()
    print("You pressed the down key!")
    
snake.direction = 'Right'
def right():
    snake.directrion = 'Right'
    move_snake()
    print("You pressed the right key!")
    
snake.direction = 'Left'
def left():
    snake.directrion = 'Left'
    move_snake()
    print("You pressed the left key!")

turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(left, 'Left')

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if snake.direction == 'Up':
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction == 'Down':
         snake.goto(x_pos, y_pos - SQUARE_SIZE)
         print("You moved down!")
    elif snake.direction == 'Right':
         snake.goto(x_pos,y_pos * SQUARE_SIZE)
         print("You moved right!")
    else snake.direction == 'Left':
         snake.goto(x_pos,y_pos / SQUARE_SIZE)
         print("You move left!")


                          
turtle.mainloop()
