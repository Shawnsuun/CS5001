from turtle import *

# Initial condition
setx(-25)
sety(-120)
scale = 20
speed(1 * scale)
bgcolor("black")
color('red')  

# Draw a rose
k = 180
for i in range (75):
    k -= 5
    circle(k, 180)
    right(45)

# Add text
penup()
goto(-50,- 150)
color('pink') 
pendown()
write("Rose Blooms for you.",font = ("Arial", 1 * scale)) 

mainloop()