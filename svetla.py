import turtle

#screen, background and title
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('carlights')

#drwing a box for front lights
pen = turtle.Turtle()
pen.color('white')
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-300,200)
pen.pendown()
pen.fd(100)
pen.rt(90)
pen.fd(50)
pen.rt(90)
pen.fd(100)
pen.rt(90)
pen.fd(50)

#drwing second box for front lights
pen2 = turtle.Turtle()
pen2.color('white')
pen2.width(3)
pen2.hideturtle()
pen2.penup()
pen2.goto(200,200)
pen2.pendown()
pen2.fd(100)
pen2.rt(90)
pen2.fd(50)
pen2.rt(90)
pen2.fd(100)
pen2.rt(90)
pen2.fd(50)