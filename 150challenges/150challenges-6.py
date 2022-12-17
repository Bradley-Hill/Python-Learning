import turtle
import random
# Challenge 60
# for i in range(0, 4):
#     turtle.forward(100)
#     turtle.left(90)
# turtle.exitonclick()
# Challenge 61
# for i in range(0, 3):
#     turtle.forward(120)
#     turtle.left(120)
# turtle.exitonclick()
# Challenge 62
# for i in range(0, 360):
#     turtle.forward(1)
#     turtle.left(1)
# turtle.exitonclick()
# # Challenge 63
# turtle.color("black", "red")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
#
# turtle.pendown()
# turtle.color("black", "yellow")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)
#
# turtle.pendown()
# turtle.color("black", "blue")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.exitonclick()
# Challenge 64
# for i in range (0, 5):
#     turtle.forward(120)
#     turtle.right(144)
# Challenge 65
# turtle.left(90)
# turtle.forward(120)
# turtle.left(180)
# turtle.forward(120)
# turtle.left(90)
# turtle.penup()
# turtle.forward(135)
# turtle.pendown()
# turtle.left(180)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(60)
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(60)
# turtle.left(90)
# turtle.forward(100)
# turtle.penup()
# turtle.left(90)
# turtle.forward(120)
# turtle.left(90)
# turtle.forward(135)
# turtle.pendown()
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(60)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(180)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(60)
# turtle.left(90)
# turtle.forward(100)
# turtle.exitonclick()
# Challenge 66
# listOfcolours = ["red", "blue", "green", "black", "yellow", "pink"]
# turtle.pensize(5)
# for i in range(0, 8):
#     turtle.color(random.choice(listOfcolours))
#     turtle.begin_fill()
#     turtle.forward(100)
#     turtle.right(45)
#     turtle.end_fill()
# Challenge 67
# for i in range(0, 10):
#     turtle.left(36)
#     for i in range(0, 8):
#         turtle.forward(100)
#         turtle.left(45)
# turtle.exitonclick()
# Challenge 68
randomAngle = random.randint(1, 365)
randomLength = random.randint(25, 125)
randomSides = random.randint(5, 30)
for i in range(0, randomSides):
    turtle.forward(randomLength)
    turtle.left(randomAngle)
turtle.exitonclick()