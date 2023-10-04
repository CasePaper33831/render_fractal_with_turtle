'''
If you wish to have fun with the code, go ahead, have fun
TODO: to be anounced

FINIFHED:
user input for popup size and iterations
'''
import turtle
import time

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def render_fractal():
    popup_size = int(input("Enter pixel size (popup will be equal in length and width): "))
    zoom = float(input("Enter zoom amount: "))
    max_iter = int(input("Enter iteration amount: "))

    width = height = popup_size

    turtle.setup(width=width, height=height)
    screen = turtle.Screen()
    screen.tracer(0)
    turtle.penup()
    turtle.goto(-width/2, -height/2)
    turtle.pendown()
    start_time = time.time()
    for x in range(width):
        for y in range(height):
            zx = (x - width/2) / (0.5 * zoom * width)
            zy = (y - height/2) / (0.5 * zoom * height)
            c = complex(zx, zy)
            color = mandelbrot(c, max_iter)
            turtle.pencolor(color / max_iter, 0, 0)
            turtle.goto(x - width/2, y - height/2)
            turtle.pendown()
            turtle.forward(1)
    end_time = time.time()
    render_time = end_time - start_time
    screen.update()

    turtle.title(f"this took: {render_time:.2f} seconds to render")

    turtle.done()

render_fractal()
