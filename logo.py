import turtle


t1 = turtle.Turtle()
t1.pensize(10)
t1.color("black")
t1.penup()
t1.goto(-80, 0)  
t1.pendown()

t2 = turtle.Turtle()
t2.pensize(10)
t2.color("blue")  
t2.penup()
t2.goto(80, -10) 
t2.pendown()

t3 = turtle.Turtle()
t3.pensize(10)
t3.color("black")
t3.penup()
t3.goto(100, 0)  
t3.pendown()

t1.left(90)
t1.forward(100)
t1.right(-90)
t1.circle(30, extent=-170)
t1.right(60)
t1.forward(60)

t2.left(90)
t2.forward(120)
t2.backward(120)
t2.left(40)
t2.forward(155)
t2.left(139)
t2.forward(120)

t3.left(90)
t3.forward(100)
t3.right(-90)
t3.circle(30, extent=-170)
t3.right(60)
t3.forward(60)

turtle.done()
