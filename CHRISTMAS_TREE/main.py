# CHRISTMAS TREE DRAWING
# using Python Turtle
# 
# the code snippets and pattern algorithms included in this project
# are collected, edited and cleaned up by STEAM GIA THIEU.
# feel free to edit and share your favourite tree to your homie=).
#
# References: Python Turtle Documentation: https://docs.python.org/3/library/turtle.html#
# Our GitHub: https://github.com/sgtsince2022
# MERRY CHRISTMAS again from SGT!!!

from property import *

""" init(background_color, show_turtle)
    
    background_color: color strings (black is default),
    show_turtle: 1 => show 
                 0 => hide (faster drawing speed)
"""
init('black', 0)

# CONTENT ADJUSTING AREA (try and see =))
## snowflakes
snowflakes_amount = 120 
## tree and ornaments
height = 100.0
tree_size = 14 
tree_color = LIGHT_GREEN
light_color1 = 'tomato'
light_color2 = 'orange'
## below the tree
btt_color1 = 'tomato'
btt_color2 = 'wheat'
btt_color3 = PINK
## message
ms_content = "MERRY CHRISTMAS!"
ms_color = LIKELY_CYAN
ms_size = 30




# int main() {
drawsnow(snowflakes_amount)  
up(); goto(0, 0); pd()
drawstar(height)
color(tree_color); backward(height * 4.8)
tree(tree_size, height, tree_color, light_color1, light_color2)
trunk(height)
below_tree(200, 'tomato', 'wheat', PINK)
message(ms_content, ms_color, ms_size)

# some additional stuffs - remove if u want our logo and infs disappear.
# from here
crdir = os.getcwd()
t1 = Turtle()
t2 = Turtle()
wn = Screen()

t1.goto(-430.0,-344.0)
wn.addshape(crdir + '\\CHRISTMAS_TREE\\asset\\LOGO.gif')
t1.shape(crdir + '\\CHRISTMAS_TREE\\asset\\LOGO.gif')

t2.goto(420.0,-344.0)
wn.addshape(crdir + '\\CHRISTMAS_TREE\\asset\\QR.gif')
t2.shape(crdir + '\\CHRISTMAS_TREE\\asset\\QR.gif')
# to here

t.done()  
# return 0;
# } =)
