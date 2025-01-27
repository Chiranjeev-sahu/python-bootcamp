from turtle import Turtle,Screen

my_screen=Screen()
donatello=Turtle()
print(my_screen.canvheight)
donatello.shape('turtle')
donatello.color('purple')
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward (200)
donatello.home()



#new
rafael=Turtle()
rafael.color('red')
rafael.shape('turtle')
rafael.penup()
rafael.goto(-150,200)
rafael.pendown()
rafael.pencolor('blue')

x=10
while x<=50:
    rafael.circle(x)
    donatello.circle(x+5)
    x+=10




my_screen.exitonclick()


