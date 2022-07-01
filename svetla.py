import turtle

#screen, background and title
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('carlights')

#drwing a box for front left light
penleft = turtle.Turtle()
penleft.color('white')
penleft.width(3)
penleft.hideturtle()
penleft.penup()
penleft.goto(-300,200)
penleft.pendown()
penleft.fd(100)
penleft.rt(90)
penleft.fd(50)
penleft.rt(90)
penleft.fd(100)
penleft.rt(90)
penleft.fd(50)

#drwaing a white front left light
whiteleft = turtle.Turtle()
whiteleft.shape('square')
whiteleft.color('grey')
whiteleft.shapesize(2.3,3.3,)
whiteleft.goto(-235,175)

#drawing a turning front left light
yellowleft = turtle.Turtle()
yellowleft.shape('square')
yellowleft.color('grey')
yellowleft.shapesize(2.3,1.5,)
yellowleft.goto(-284,175)

#drwing a box for front right light
penright = turtle.Turtle()
penright.color('white')
penright.width(3)
penright.hideturtle()
penright.penup()
penright.goto(200,200)
penright.pendown()
penright.fd(100)
penright.rt(90)
penright.fd(50)
penright.rt(90)
penright.fd(100)
penright.rt(90)
penright.fd(50)

#drwaing a white front right light
whiteright = turtle.Turtle()
whiteright.shape('square')
whiteright.color('grey')
whiteright.shapesize(2.3,3.3,)
whiteright.goto(235,175)

#drawing a turning front left light
yellowright = turtle.Turtle()
yellowright.shape('square')
yellowright.color('grey')
yellowright.shapesize(2.3,1.5,)
yellowright.goto(284,175)

#drwing a box for back left light
penleft2 = turtle.Turtle()
penleft2.color('red')
penleft2.width(3)
penleft2.hideturtle()
penleft2.penup()
penleft2.goto(-250,-200)
penleft2.pendown()
penleft2.fd(100)
penleft2.rt(90)
penleft2.fd(50)
penleft2.rt(90)
penleft2.fd(100)
penleft2.rt(90)
penleft2.fd(50)

#drwaing a red back left light
redleft = turtle.Turtle()
redleft.shape('square')
redleft.color('grey')
redleft.shapesize(2.3,3.3,)
redleft.goto(-185,-225)

#drawing a turning back left light
yellowleft2 = turtle.Turtle()
yellowleft2.shape('square')
yellowleft2.color('grey')
yellowleft2.shapesize(2.3,1.5,)
yellowleft2.goto(-234,-225)

#drwing a box for back right light
penright2= turtle.Turtle()
penright2.color('red')
penright2.width(3)
penright2.hideturtle()
penright2.penup()
penright2.goto(150,-200)
penright2.pendown()
penright2.fd(100)
penright2.rt(90)
penright2.fd(50)
penright2.rt(90)
penright2.fd(100)
penright2.rt(90)
penright2.fd(50)

#drwaing a red back right light
redright2 = turtle.Turtle()
redright2.shape('square')
redright2.color('grey')
redright2.shapesize(2.3,3.3,)
redright2.goto(185,-225)

#drawing a turning back left light
yellowright2= turtle.Turtle()
yellowright2.shape('square')
yellowright2.color('grey')
yellowright2.shapesize(2.3,1.5,)
yellowright2.goto(234,-225)


