from graph import *

windowSize(600, 600)
canvasSize(600, 600)

# рисование
penColor("black")
brushColor("blue")
rectangle(1, 1, 599, 599)

# рисование полос
penColor(100, 100, 255)
for i in range(0, 600, 20):
    line(i, 0, i, 600)
for i in range(00, 600, 20):
    line(0, i, 600, i)

penColor("red")
brushColor("yellow")
# создание змейки
snake = []
snake_leng = 10
snake_x_nachalo = 300
snake_y_nachalo = 300
def snake_create():
    for i in range(0, snake_leng, 1):
        snake.append(rectangle((snake_x_nachalo + i*20), snake_y_nachalo, (snake_x_nachalo + i*20 +20), (snake_y_nachalo + 20)))
    changeFillColor(snake[0], "red")


def move_snake():
    for i in range((snake_leng - 1), 0, -1):
        newCoord = coords(snake[i-1])
        moveObjectTo(snake[i], (newCoord[0] + 1), (newCoord[1] + 1))
# !!!!!!!!!!!!
    newCoord = coords(snake[0])
    moveObjectTo(snake[0], (newCoord[0] + 1 + 20*dx), (newCoord[1] + 1 + 20*dy))
    for j in range((snake_leng - 1), 0, -1):
        if coords(snake[0]) == coords(snake[j]):
            close()
def keyPressed(event):
    global dx, dy
    if event.keycode == VK_ESCAPE:
        close()
    if event.keycode == VK_LEFT:

        dx = -1
        dy = 0
    elif event.keycode == VK_RIGHT:
        dx = 1
        dy = 0
    elif event.keycode == VK_UP:
        dx = 0
        dy = -1
    elif event.keycode == VK_DOWN:
        dx = 0
        dy = 1
# ======================






dx = -1
dy = 0

snake_create()


onKey(keyPressed)

onTimer(move_snake, 1000)

run()
