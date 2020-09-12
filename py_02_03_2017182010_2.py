import turtle
count =0
while(count <=5):
	turtle.penup()
	turtle.goto(250,250+count*(-100))
	turtle.pendown()
	turtle.goto(-250,250+count*(-100))
	count =count+1
count =0
while(count <=5):
    turtle.penup()
    turtle.goto(250+count*(-100),250)
    turtle.pendown()
    turtle.goto(250+count*(-100),-250)
    count = count +1

turtle.exitonclick()

    
