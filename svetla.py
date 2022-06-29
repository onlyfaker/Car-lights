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

