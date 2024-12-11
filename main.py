import turtle


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Presentation")
screen.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


pages = [
    {"title": "Introduction", "text": "Ahmed Suhails Presentation", "color": "lightblue", "shape": "circle"},
    {"title": "Favorite Foods", "text": "Pizza Sushi and Pasta", "color": "lightpink", "shape": "rectangle"},
    {"title": "Hobbies", "text": "Painting PLaying and Playing guitar", "color": "lightgreen", "shape": "triangle"},
    {"title": "Favorite Movie", "text": "Oppenheimer", "color": "lightyellow", "shape": "star"},
    {"title": "Favorite Sport", "text": "Badminton", "color": "lightpurple", "shape": "square"},
]

current_page = 0


def draw_circle():
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    pen.circle(100)


def draw_rectangle():
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    for _ in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(100)
        pen.left(90)


def draw_triangle():
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    for _ in range(3):
        pen.forward(200)
        pen.left(120)


def draw_star():
    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    for _ in range(5):
        pen.forward(200)
        pen.right(144)


def draw_square():
    pen.penup()
    pen.goto(-100, -100)
    pen.pendown()
    for _ in range(4):
        pen.forward(200)
        pen.left(90)


shape_draw_functions = {
    "circle": draw_circle,
    "rectangle": draw_rectangle,
    "triangle": draw_triangle,
    "star": draw_star,
    "square": draw_square,
}


def draw_page():
    global current_page
    screen.bgcolor(pages[current_page]["color"])
    pen.clear()


    pen.penup()
    pen.goto(0, 200)
    pen.write(pages[current_page]["title"], align="center", font=("Arial", 24, "bold"))


    pen.goto(0, 150)
    pen.write(pages[current_page]["text"], align="center", font=("Arial", 18, "normal"))


    shape_draw_functions[pages[current_page]["shape"]]()


    pen.penup()
    pen.goto(0, -200)
    pen.write("Press Enter to continue", align="center", font=("Arial", 16, "italic"))


def next_page():
    global current_page
    current_page = (current_page + 1) % len(pages)
    draw_page()


screen.listen()
screen.onkey(next_page, "Return")


draw_page()


screen.mainloop()
