import turtle
import math
import random

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

enemies = []

for i in range(5):
    enemy = turtle.Turtle()
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.goto(random.randint(-300, 300), random.randint(100, 250))
    enemies.append(enemy)

enemy_speed = 2

score = 0

score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-330, 260)
score_pen.write("Score: 0", font=("Arial", 16, "normal"))

lives = 3

lives_pen = turtle.Turtle()
lives_pen.color("white")
lives_pen.penup()
lives_pen.hideturtle()
lives_pen.goto(230, 260)
lives_pen.write("Lives: 3", font=("Arial", 16, "normal"))
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

def is_collision(t1, t2):
    distance = math.sqrt((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2)
    return distance < 25
while True:
    screen.update()

    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        if enemy.xcor() > 330:
            enemy_speed *= -1
            for e in enemies:
                e.sety(e.ycor() - 40)

        if enemy.xcor() < -330:
            enemy_speed *= -1
            for e in enemies:
                e.sety(e.ycor() - 40)

        if enemy.ycor() < -250:
            lives -= 1

            lives_pen.clear()
            lives_pen.write(f"Lives: {lives}", font=("Arial", 16, "normal"))

            enemy.goto(random.randint(-300, 300), 250)

            if lives == 0:
                player.hideturtle()
                bullet.hideturtle()

                for e in enemies:
                    e.hideturtle()

                game_over = turtle.Turtle()
                game_over.color("red")
                game_over.hideturtle()
                game_over.write("GAME OVER", align="center", font=("Arial", 30, "bold"))

                enemy_speed = 0

    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

        for enemy in enemies:
            if is_collision(bullet, enemy):
                bullet.hideturtle()
                bullet_state = "ready"
                bullet.goto(0, -400)

                enemy.goto(random.randint(-300, 300), random.randint(100, 250))

                score += 1
                score_pen.clear()
                score_pen.write(f"Score: {score}", font=("Arial", 16, "normal"))

        if y > 300:
            bullet.hideturtle()
            bullet_state = "ready"