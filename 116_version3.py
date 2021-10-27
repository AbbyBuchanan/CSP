#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider_body is used
spider_body = trtl.Turtle()
#create spider body
spider_body.pensize(40)
spider_body.circle(20)
#configure spider legs
num_legs = 8
leg_length = 100
dis_between_legs = 360 / num_legs
spider_body.pensize(5)
#draw legs
legs_drawn = 0
while (legs_drawn < num_legs):
  spider_body.goto(0,20)
  spider_body.setheading(dis_between_legs*legs_drawn)
  spider_body.forward(leg_length)
  legs_drawn = legs_drawn + 1
spider_body.penup()
spider_body.setposition(20,20)
spider_body.pendown()
spider_body.color("red")
spider_body.begin_fill()
spider_body.circle(5)
spider_body.end_fill()

spider_body.penup()
spider_body.setposition(12.5,30)
spider_body.pendown()
spider_body.color("red")
spider_body.begin_fill()
spider_body.circle(5)
spider_body.end_fill()

spider_body.hideturtle() 
wn = trtl.Screen() 
wn.mainloop()