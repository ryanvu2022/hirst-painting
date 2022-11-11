# import colorgram
import turtle
import random

x = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()

# Extract color from Damien Hirst's Spot Painting.
# colors = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

x.speed("fastest")
x.hideturtle()

x_axis = -240
y_axis = -220
gap = 50
x.penup()
x.goto(x_axis, y_axis)

row = 1
while row < 11:
    for _ in range(10):
        x.pendown()
        x.dot(20, random.choice(color_list))
        x.penup()
        x.forward(gap)
    row += 1
    y_axis += gap
    x.goto(x_axis, y_axis)

screen.exitonclick()
