'''TODO: 
user input for popup size and iterations
'''
import turtle

def mandelbrot(c, max_iter):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

def render_fractal(width, height, zoom, max_iter):
    turtle.setup(width=width, height=height)
    screen = turtle.Screen()
    screen.tracer(0)
    turtle.penup()
    turtle.goto(-width/2, -height/2)
    turtle.pendown()
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
    screen.update()
    turtle.done()

render_fractal(1500, 1500, 1, 100)
