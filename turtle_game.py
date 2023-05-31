import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle Game")

turtle_instance = turtle.Turtle()
def turtle_forward():
    turtle_instance.forward(100)
def turtle_right():
    turtle_instance.right(45)
def clear_screen():
    turtle_instance.clear()
def zero_point():
    turtle_instance.home()
drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=turtle_right, key="Up")
drawing_board.onkey(fun=clear_screen, key="x")
drawing_board.onkey(fun=zero_point, key="b")
turtle.mainloop()