import turtle
import time
from random import randint

#sabitler
game_over = False
drawing_board = turtle.Screen()
drawing_board.title("Catch The Turtle")
drawing_board.bgcolor("#3386FF")
FONT = ("Times New Roman", 20, "normal")
score = 0
timer_turtle = turtle.Turtle()
score_turtle= turtle.Turtle()
turtle_instance = turtle.Turtle()

def skor_tahtası():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.sety(250)
    score_turtle.clear()
    score_turtle.write(arg=f"Score: {score} ", move=False, align="center", font=FONT)

def countdown(time):
    global game_over
    timer_turtle.penup()
    timer_turtle.sety(225)
    timer_turtle.setx(-10)
    timer_turtle.hideturtle()
    timer_turtle.clear()

    if time > 0:
        timer_turtle.clear()
        timer_turtle.write(f"Time: {time}", move=False,align="center", font=FONT)
        drawing_board.ontimer(lambda: countdown(time - 1), 1000)

    else:
        game_over = True
        timer_turtle.clear()
        timer_turtle.write("Game Over!", align='center', font=FONT)

def turtle_move():
    turtle_instance.penup()
    turtle_instance.speed(0)
    turtle_instance.shape("turtle")
    turtle_instance.showturtle()
    turtle_instance.color("green")
    x = 0
    back_count = 9
    while x <= back_count:
        turtle_instance.hideturtle()
        turtle_instance.goto(x=randint(-275, 275), y=randint(-275, 275))
        x += 1
        turtle_instance.showturtle()
        time.sleep(1)
        turtle_instance.hideturtle()
    def score_plus():
        global score
        score += 1
        score_turtle.write(arg=f"Score: {score} ", move=False, align="center", font=FONT)

def oyun_baslasin():
    skor_tahtası()
    countdown(10)
    turtle_move()

oyun_baslasin()
turtle.mainloop()