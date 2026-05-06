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

player_speed = 20


def move_left():
    x = player.xcor()
    x -= player_speed

    if x < -330:
        x = -330

    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed

    if x > 330:
        x = 330

    player.setx(x)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

turtle.done()