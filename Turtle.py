import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("#33FFD1")  #HTML color codes.
drawing_board.title("Python Turtle")

#square
'''
turtle_instance= turtle.Turtle()
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
'''
'''
x = 0
turtle_instance = turtle.Turtle()
while x < 4:
    turtle_instance.forward(100)
    turtle_instance.right(90)
    x+=1
    continue
for i range(4)
    turtle_instance.forward(100)
    turtle_instance.right(90) komutu ilede olurdu.
''' # turtle_instance = turtle.Turtle() ifadesi while içinde olursa her seferde yeni turtle nesnesi
#oluşturucağından kare oluşmazdı, ileri sağ ileri yapar olduğu konumda dururdu, fakat nesne dışarda olunca karede oluştu.
#turtle.done()
#star
'''
turtle_instance = turtle.Turtle()
turtle_instance.right(72)
turtle_instance.forward(100)
turtle_instance.right(144)
turtle_instance.forward(100)
turtle_instance.left(72)
turtle_instance.forward(100)
turtle_instance.right(144)
turtle_instance.forward(100)
turtle_instance.left(72)
turtle_instance.forward(100)
turtle_instance.right(144)
turtle_instance.forward(100)
turtle_instance.left(72)
turtle_instance.forward(100)
turtle_instance.right(144)
turtle_instance.forward(100)
turtle_instance.left(72)
turtle_instance.forward(100)
turtle_instance.right(144)
turtle_instance.forward(100)
turtle.done()

turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(200)
turtle.done()
'''
'''#polygon
num_side = 5
angle = 360/num_side
side_length = 150
turtle_instance = turtle.Turtle()
for i in range(num_side):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)
turtle.done()
'''
line_length= 45
square_num =10
loop_num = square_num * 4
turtle_instance = turtle.Turtle()
for i in range(loop_num):
    turtle_instance.forward(line_length)
    turtle_instance.right(90)
    line_length+=15
turtle.done()
