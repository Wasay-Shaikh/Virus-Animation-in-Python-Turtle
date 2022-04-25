
# Virus In Python

import turtle as tr

a = 0
b = 0
tr.bgcolor('black')
tr.speed(0)
tr.pencolor('green')
tr.penup()
tr.goto(0, 200)
tr.pendown()

while True:
    tr.forward(a)
    tr.right(b)
    a += 3
    b += 1