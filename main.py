import turtle

screen = turtle.Screen()
screen.title("Cosmic Blaster")
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.tracer(0)

player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -250)

player_speed = 20

bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.3, stretch_len=0.8)
bullet.penup()
bullet.hideturtle()

bullet_speed = 20
bullet_state = "ready"

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

def fire_bullet():
    global bullet_state

    if bullet_state == "ready":
        bullet_state = "fire"

        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

while True:

    screen.update()

    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

        if y > 300:
            bullet.hideturtle()
            bullet_state = "ready"