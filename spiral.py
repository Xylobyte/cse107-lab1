#Draws a spiral with 128 lines and a givven angle
import turtle

angle = int(input("Give an angle: "))
pen = turtle.Turtle()
pen.speed(0.5)
window = turtle.Screen()
length = 10

for i in range(128):
    pen.forward(length)
    pen.right(angle)
    length += 2
window.mainloop()
