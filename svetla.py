import turtle

#screen, background and title
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('carlights')

#drwing a box for front lights
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

#drwaing a white light
whiteleft = turtle.Turtle()
whiteleft.shape('square')
whiteleft.color('grey')
whiteleft.shapesize(2.3,3.3,)
whiteleft.goto(-235,175)

#drawing a turning front light
yellow = turtle.Turtle()
yellow.shape('square')
yellow.color('grey')
yellow.shapesize(2.3,1.5,)
yellow.goto(-284,175)

# #drwing second box for front lights
# penright = turtle.Turtle()
# penright.color('white')
# penright.width(3)
# penright.hideturtle()
# penright.penup()
# penright.goto(200,200)
# penright.pendown()
# penright.fd(100)
# penright.rt(90)
# penright.fd(50)
# penright.rt(90)
# penright.fd(100)
# penright.rt(90)
# penright.fd(50)

