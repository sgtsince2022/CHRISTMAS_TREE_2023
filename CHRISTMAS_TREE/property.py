import turtle as t  
from turtle import *
import random as r
import time
import os

# Bảng màu - COLORS DEFINITIONS
## add thêm màu ở đây
LIKELY_CYAN = '#52ebeb'
LIGHT_GREEN = '#42f587'
LIGHT_BLUE = '#42b3f5'
LIKELY_BROWN = '#c97538'
BLUE_TO_BROWN_TRANS = '#7fbc63'
PINK = '#f046df'

def init(bgcolor: str = 'black', show_turtle: bool = 0):  
    screensize(bg='black')  
    speed(0) 
    if show_turtle == 1:
        st() 
    else:
        ht()

def drawsnow(amount: int = 120, density: int = 5, maxSize: int = 7):  
    t.pensize(2) 
    for i in range(amount): 
        t.pencolor("white")  
        t.pu() 
        t.setx(r.randint(-350, 350))  
        t.sety(r.randint(-100, 350)) 
        t.pd()  
        dens = density
        snowsize = r.randint(1, maxSize) 
        for j in range(dens): 
            t.forward(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360 / dens))

def drawstar(tree_height: float):
    left(90)
    forward(3 * tree_height)
    color("orange", "yellow")  
    begin_fill()
    left(126)

    for i in range(5):  
        forward(tree_height / 5)
        right(144)  
        forward(tree_height / 5)
        left(72)  
    end_fill()

    right(126)

def drawlight(color1: str = 'tomato', color2: str = 'orange'):  
    if r.randint(0, 40) == 0:  
        color(color1)  
        begin_fill()
        circle(6)  
        end_fill()
    elif r.randint(0, 30) == 1:
        color(color2)  
        begin_fill()
        circle(3)  
        end_fill()
    else:
        color(LIGHT_GREEN)  

def tree(d, s, color_tree: str = LIGHT_GREEN, color_light_1: str = 'tomato', color_light_2: str = 'orange'):
    color(color_tree)  
    pensize(1)
    if d <= 0: return
    forward(s)
    tree(d - 1, s * .8)
    right(120)
    tree(d - 3, s * .5)
    drawlight(color_light_1, color_light_2)  
    right(120)
    tree(d - 3, s * .5)
    right(120)  
    backward(s)

def trunk(tree_height: float):
    pensize(2)
    color(BLUE_TO_BROWN_TRANS)
    backward(10.0)
    color(LIKELY_BROWN)
    backward(25.0)
    color('black')
    backward(50.0)
    color(LIKELY_BROWN)
    backward(tree_height - 75.0)

def below_tree(amount: int, color1: str, color2: str, color3: str):
    pensize(2)
    for i in range(amount):  
        a = 200 - 400 * r.random()
        b = 10 - 20 * r.random()
        up()
        forward(b)
        left(90)
        forward(a)
        down()
        random_color = r.randint(0, 2) 
        if random_color == 0:
            color(color1)
        elif random_color == 1:
            color(color2)
        else:
            color(color3)
        circle(2)
        up()    
        backward(a)
        right(90)
        backward(b)

def message(mainms: str = "MERRY CHRISTMAS!", mscolor: str = LIKELY_CYAN, mssize: int = 30):
    style1 = ("Comic Sans MS", mssize, "bold")
    forward(25)
    t.color(mscolor, mscolor) 
    t.write(mainms, align = "center", font = style1)

    # additional hehe=)
    style2 = ("Comic Sans MS", 15, "italic")
    backward(125)
    t.color(LIGHT_BLUE, LIGHT_BLUE) 
    t.write("\nfrom\n", align = "center", font = style2)  
    t.write("STEAM GIA THIEU=)", align = "center", font = style2)  