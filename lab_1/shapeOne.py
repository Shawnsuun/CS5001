from turtle import *

# Write text "I"
penup()
goto(-400,-60)
color('black') 
pendown()
write("I",font = ("Arial", 200)) 

# Draw a red heart
penup()
setx(-150)
sety(0)
pendown()
scale = 60
color('pink','red')        
begin_fill()
left(135)
forward(2 * scale)
circle(-1 * scale, 180)
left(90)
circle(-1 * scale, 180)
forward(2* scale)       
end_fill()

# Write text "NEU"
penup()
goto(0,-60)
color('black') 
pendown()
write("NEU",font = ("Arial", 200)) 

done()