#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider_body is used
spider_body = trtl.Turtle()
spider_body.pensize(40)
spider_body.circle(20)
num_legs = 8
leg_length = 100
dis_between_legs = 360 / num_legs
spider_body.pensize(5)
legs_drawn = 0
while (legs_drawn < num_legs):
  spider_body.goto(0,0)
  spider_body.setheading(dis_between_legs*legs_drawn)
  spider_body.forward(leg_length)
  legs_drawn = legs_drawn + 1
spider_body.hideturtle() 
wn = trtl.Screen() 
wn.mainloop()