import turtle

def draw_circle(x,y,r):
    for a,b,c in [(x,y,r)]:
        turtle.penup()
        turtle.goto(a,b)
        turtle.pendown()
        turtle.circle(c)
        turtle.write((a,b))




turtle.shape("turtle")

draw_circle(0,0,50)
draw_circle(200,200,100)
draw_circle(100,-100,50)
        
