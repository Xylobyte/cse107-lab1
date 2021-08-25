'''
Ask the user to enter a positive integer. 
Then consecutively draw shapes with 3, 4, 5, 6, and 7 sides where the side length of each is the user ’s input.
'''

import turtle
shapes = 7

length = int(input("Enter a positive integer: "))
window = turtle.Screen()
pen = turtle.Turtle()
pen.setx(-300)

for i in range(shapes + 1):
    if i < 3:
        continue
    for j in range(i):
        pen.forward(length)
        pen.left(360 / i)
    pen.forward(2.5 * length)

window.mainloop()
