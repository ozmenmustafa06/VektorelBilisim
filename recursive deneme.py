import turtle
def star(turtle, n,r):

 for k in range(0,n):
    turtle.speed(100)
    turtle.pendown()
    turtle.forward(r)
    turtle.penup()
    turtle.backward(r)
    turtle.left(360/n)
 
def recursive_star(turtle, n, r, depth, f):
 
 if depth == 0:
    star(turtle, n, f*4)
 else:
    for k in range(0,n):
        turtle.speed(100)
        turtle.pendown()
        turtle.forward(r)
        recursive_star(turtle, n, f*r, depth - 1,f)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360/n)
 
turtle.speed("fastest")
recursive_star(turtle, 5 , 150, 4, 0.4)
input()