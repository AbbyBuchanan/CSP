# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2
score = 0

#-----initialize turtle-----
spot = trtl.Turtle()
spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_size)

#-----game functions--------
spot.penup()
def spot_clicked(x,y):
  change_position()
def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)
#-----events----------------
wn = trtl.Screen()
spot.onclick(spot_clicked)
wn.mainloop()