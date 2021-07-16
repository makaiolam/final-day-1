import turtle

# turtle = turtle.Turtle()
# shape = input("choose shape triangle square or circle")

# if shape == ("triangle"):
#   def triangle(length,color):
#     turtle.speed(1)
#     turtle.color(color)
#     turtle.forward(length)
#     turtle.left(120)
#     turtle.forward(length)
#     turtle.left(120)
#     turtle.forward(length)
#   c = input("choose a color black or red")
#   l = input("choose a length for the triangle, 100 or 50")
#   triangle(l,c)



# elif shape == ("square"):
#   def square(length, color):
#     turtle.speed(1)
#     turtle.color(color)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#   c = input("choose a color black or red")
#   l = input("choose a length for the triangle, 100 or 50")
#   square(l,c)

# if shape == ("circle"):
#   def circle(length,color):
#     turtle.circle(length)
#   c = input("choose a color red or black:")
#   l = input("choose a length 100 or 50:")
#   circle(l,c)

# window = turtle.Screen()
# window.setup(500,500)

# turtle = turtle.Turtle()
window = turtle.Screen()
window.setup(500,500)

turtle = turtle.Turtle()


def drawcircle():
  turtle.circle(100)
  turtle.speed(15)
def pattern1():
 x = 0
 while x < 36:
   drawcircle()
   turtle.right(50)
   x += 1
pattern1()



def drawcircle2():
  turtle.circle(50)
  turtle.speed(10)
def circle():
  x = 0
  while x < 26:
    drawcircle()
    turtle.left(100)
    x =+ 1
circle()
# window = turtle.Screen()
# window.setup(500,500)

# turtle = turtle.Turtle()


# def drawcircle():
#   turtle.circle(100)
#   turtle.speed(15)
# def pattern1():
#  x = 0
#  while x < 36:
#    drawcircle()
#    turtle.right(50)
#    x += 1
# pattern1()






