import turtle

def draw_circle_head(color, radius, x, y):
    turtle.penup()
    turtle.pencolor(color)
    turtle.pensize(width=3)
    turtle.fillcolor("white")
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.pencolor(color)
    turtle.fillcolor("#800047")
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_line(color, x1, y1, x2, y2, width):
    turtle.penup()
    turtle.pencolor(color)
    turtle.pensize(width)
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def draw_line_lip(color, x1, y1, x2, y2, width):
    turtle.penup()
    turtle.pencolor(color)
    turtle.pensize(width)
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def draw_text(text, x, y, size=16):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.write(text, align="center", font=("Helvetica", size, "normal"))

def main():
    turtle.speed(15)                                                    

    draw_circle_head("blue", 50, 0, 200) 				
    draw_circle("white", 10, -20, 215)  				
    draw_circle("white", 10, 20, 215) 					
    draw_line_lip("red", -26, 180, 26, 180, 6)				
    draw_line("yellow", 0, 150, 0, -25, 1.5) 				
    draw_line("violet", 0, 75, -75, 100, 1.5)  				
    draw_line("#90EE90", 0, 75, 75, 100, 1.5) 				
    draw_line("red", 0, -25, -75, -125, 1.5) 				
    draw_line("red", 0, -25, 75, -125, 1.5)  				

    draw_text("Carlos Miguel Reopirio", 0, -300)                  

    turtle.hideturtle()
    turtle.done()

main()
