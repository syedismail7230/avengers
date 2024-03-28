import turtle

canvas1 = [[(-100, 90), (-70, 60), (-30, 30), (-70, 0), (-70, 00), (-60, 40), (-10, 10), (-50, -10), (-140, 10),
           (-40, -20), (0, -20)],
          [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
           (40, 120), (0, 120)]]
canvas2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
           (-80, -230), (-64, -210), (0, -210)],
          [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
           (100, -46), (50, -40), (40, -30), (0, -30)]]
canvas3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
           (0, -250)],
          [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
           (0, -220)]]

turtle.hideturtle()
turtle.bgcolor('#000000')  
turtle.setup(500, 600)
turtle.title("I AM IRONMAN")
canvas1Goto = (0, 120)
canvas2Goto = (0, -30)
canvas3Goto = (0, -220)
turtle.speed(2)


def logo(a, b):
    turtle.penup()
    turtle.goto(b)
    turtle.pendown()
    turtle.color('#2a2a2a')  # Light Yellow
    turtle.begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        turtle.goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        turtle.goto(x, y)
    turtle.end_fill()


logo(canvas1, canvas1Goto)
logo(canvas2, canvas2Goto)
logo(canvas3, canvas3Goto)
turtle.hideturtle()
turtle.done()