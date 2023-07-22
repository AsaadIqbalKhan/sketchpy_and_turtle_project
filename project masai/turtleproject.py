import turtle
pointer=turtle.Turtle()
pointer.color('red')
pointer.pensize(5)
for i in range(10,100,30):
    pointer.circle(i,360)
    pointer.right(10)
pointer.forward(70)
pointer.color('green')
for i in range(4):
    pointer.right(144)
    pointer.forward(100)
pointer.left(90)
pointer.pensize(0)
pointer.color('white')
pointer.forward(150)
pointer.color('black')
pointer.right(90)
pointer.forward(150)
pointer.pensize(5)
for i in range(4):
    pointer.right(90)
    pointer.forward(360)
pointer.circle(20,180)
pointer.clear()


p=pointer
turtle.Screen().bgcolor("lightgreen")
p.setheading(0)
p.right(90)

p.fillcolor("red")
p.begin_fill() 
for i in range(2):
    p.forward(200)
    p.right(90)
    p.forward(100)
    p.right(90)
p.end_fill() 
p.left(90)
for i in range(4):
    p.forward(200)
    p.right(90)
p.clear()


colors=["yellow","red","blue","pink","green","black","orange"]
p.speed(5)
for i in range(3):
    p.fillcolor(colors[i])
    p.begin_fill() 
    for i in range(6):
        p.forward(90)
        p.left(300)
    p.end_fill() 
p.clear()


p.speed(10)
p.pensize(3)
for i in range(7):
    p.fillcolor(colors[i])
    p.begin_fill()
    for i in range(5):
        pointer.right(144)
        pointer.forward(200)
    p.end_fill()
p.speed(1)
p.pensize(20)
p.forward(500)
p.clear()
turtle.done()
