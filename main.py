import turtle

screen = turtle.Screen()
screen.title("Cosmic Blaster")
screen.bgcolor("black")
screen.setup(width=700, height=600)

player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -250)

turtle.done()