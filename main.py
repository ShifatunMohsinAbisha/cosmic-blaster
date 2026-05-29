import turtle
import math
import random

screen = turtle.Screen()
screen.title("Cosmic Blaster")
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.tracer(0)

meteor_shape = (
    (-10, 15),
    (5, 20),
    (18, 8),
    (14, -10),
    (0, -18),
    (-15, -12),
    (-20, 5)
)
screen.register_shape("meteor", meteor_shape)

player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.goto(0, -250)

player_speed = 20

score = 0
lives = 3

score_pen = turtle.Turtle()
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-330, 260)
score_pen.write("Score: 0", font=("Arial", 16, "normal"))

lives_pen = turtle.Turtle()
lives_pen.color("white")
lives_pen.penup()
lives_pen.hideturtle()
lives_pen.goto(230, 260)
lives_pen.write("Lives: 3", font=("Arial", 16, "normal"))

enemies = []

for i in range(5):
    enemy = turtle.Turtle()
    enemy.shape("meteor")
    enemy.color("gray")
    enemy.penup()
    enemy.shapesize(random.uniform(1.0, 1.5), random.uniform(1.0, 1.5))
    enemy.tilt(random.randint(0, 360))
    enemy.goto(random.randint(-300, 300), random.randint(100, 250))
    enemies.append(enemy)

def click_handler(x, y):
    global score
    if lives <= 0:
        return
    for enemy in enemies:
        dist = math.sqrt((x - enemy.xcor()) ** 2 + (y - enemy.ycor()) ** 2)
        if dist < 28:
            enemy.goto(random.randint(-320, 320), random.randint(200, 280))
            enemy.tilt(random.randint(0, 360))
            score += 1
            score_pen.clear()
            score_pen.write(f"Score: {score}", font=("Arial", 16, "normal"))
            break

screen.onclick(click_handler)

def move_left():
    x = player.xcor() - player_speed
    player.setx(max(x, -330))

def move_right():
    x = player.xcor() + player_speed
    player.setx(min(x, 330))

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

game_over_pen = turtle.Turtle()
game_over_pen.color("red")
game_over_pen.penup()
game_over_pen.hideturtle()
game_over_pen.goto(0, 0)

def show_game_over():
    player.hideturtle()
    for e in enemies:
        e.hideturtle()
    game_over_pen.write("GAME OVER", align="center", font=("Arial", 30, "bold"))

game_running = True

while game_running:
    screen.update()

    for enemy in enemies:
        enemy.sety(enemy.ycor() - 2)

        if enemy.ycor() < -270:
            lives -= 1
            lives_pen.clear()
            lives_pen.write(f"Lives: {lives}", font=("Arial", 16, "normal"))
            enemy.goto(random.randint(-320, 320), random.randint(200, 280))
            enemy.tilt(random.randint(0, 360))

            if lives <= 0:
                show_game_over()
                game_running = False
                break

turtle.done()