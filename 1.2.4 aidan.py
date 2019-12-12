#Import turtle as trtl
import turtle as trtl
import random


az = trtl.Turtle()
az.shape("circle")
az.turtlesize(.4)


am = trtl.Turtle()
am.ht()
am.speed(0)
side=200
am.pensize(5)
wall_width = 8
door_width = 22

def drawDoor():
    am.penup()
    am.forward(door_width)
    am.pendown()

def drawBarrier():
    am.right(90)
    am.forward(wall_width*2)
    am.backward(wall_width*2)
    am.left(90)

def az_up():
    az.setheading(90)
    az.forward(10)

def az_down():
    az.setheading(270)
    az.forward(10)

def az_right():
    az.setheading(0)
    az.forward(10)

def az_left():
    az.setheading(180)
    az.forward(10)


for i in range(25):

    if i < 17:
        door = random.randint(0, side/2)
        barrier = random.randint(wall_width*2, side - door_width*2)
        if door < barrier:


            am.forward(door)
            drawDoor()
            am.forward(barrier - door - door_width)
        
            drawBarrier()
            am.forward(side - barrier)

        else:
            am.forward(barrier)
            drawBarrier()
            am.forward(door - barrier)
            drawDoor()
            am.forward(side - door_width - door)
        

        am.right(90)
        side = side - 8 






wn = trtl.Screen()
wn.bgcolor("light blue")
wn.onkeypress(az_up,"Up")
wn.onkeypress(az_down,"Down")
wn.onkeypress(az_left,"Left")
wn.onkeypress(az_right,"Right")


wn.listen()
wn.mainloop()
wn.bgcolor("light blue")