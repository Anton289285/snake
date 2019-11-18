from graph import *
from random import *
# =====================================================


def innicializations():
    windowSize(600, 600)
    canvasSize(600, 600)

    # рисование
    penColor("black")
    brushColor("black")
    rectangle(1, 1, 599, 599)

    # рисование полос
    penColor(100, 100, 255)
    for i in range(0, 600, 20):
        line(i, 0, i, 600)
    for i in range(00, 600, 20):
        line(0, i, 600, i)

    penColor("red")
    brushColor("yellow")

# =========================================================
Pause = True
# создание змейки


# snake = []

snake_x_nachalo = 300
snake_y_nachalo = 300
def snake_create():
    global snake
    snake = []

    brushColor("yellow")
    for i in range(0, snake_leng, 1):
        snake.append(rectangle((snake_x_nachalo + i*20), snake_y_nachalo,
                               (snake_x_nachalo + i*20 + 20),
                               (snake_y_nachalo + 20)))
    changeFillColor(snake[0], "red")
#===============================================================
coord_prize = []
coord_prize.append(randrange(0, 580, 20))
coord_prize.append(randrange(0, 580, 20))

def timer_loop():
    pass


def prize_create():
    global prize
    global coord_prize
    global snake, snake_leng
    coord_prize[0] = randrange(0, 580, 20)
    coord_prize[1] = randrange(0, 580, 20)

    brushColor(randint(0, 255), randint(0, 255), randint(0, 255))
    prize = rectangle(coord_prize[0], coord_prize[1],
                      coord_prize[0] + 20, coord_prize[1] + 20)


def remove_snake():
    for i in range(0, snake_leng, 1):
        deleteObject(snake[i])


def remove_prize():
    deleteObject(prize)


#==============================================================
def move_snake():
    global snake_leng, snake
    coord_last = coords(snake[snake_leng - 1])

    for i in range((snake_leng - 1), 0, -1):
        newCoord = coords(snake[i-1])
        moveObjectTo(snake[i], (newCoord[0] + 1), (newCoord[1] + 1))
    newCoord = coords(snake[0])
    moveObjectTo(snake[0], (newCoord[0] + 1 + 20*dx), (newCoord[1] + 1 + 20*dy))
    for j in range((snake_leng - 1), 0, -1):
        if coords(snake[0]) == coords(snake[j]):
            game_timer.func = timer_loop

    coord_0 = coords(snake[0])
    if (coord_0[0] < -1) or (coord_0[1] < -1) or (coord_0[0] > 581) or (coord_0[1] > 581):
        game_timer.func = timer_loop
    if (((coord_0[0] + 1) == coord_prize[0]) and ((coord_0[1]+1) == coord_prize[1])):
        #changeFillColor(snake[0], "green")
        moveObjectTo(prize, coord_last[0], coord_last[1])
        snake.append(prize)
        snake_leng = snake_leng + 1
        prize_create()

#=============================================


def keyPressed(event):
    global dx, dy, snake_leng, game_timer, Pause
    if event.keycode == VK_ESCAPE:
        close()
    if event.keycode == VK_RETURN:
        game_timer.func = timer_loop
        dx = -1
        dy = 0
        remove_snake()
        remove_prize()
        snake_leng = 3
        snake_create()
        prize_create()
        game_timer.func = move_snake

    if event.keycode == VK_SPACE:
        if Pause == True:
            game_timer.func = move_snake
            Pause = False
        else:
            game_timer.func = timer_loop
            Pause = True

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
snake_leng = 3
#!!!!!!!!!!!
# def main():

onKey(keyPressed)
#onTimer(movie_snake, 100)
game_timer = onTimer(timer_loop, 100)
innicializations()
snake_create()
prize_create()


run()
#!!!!!!!!!
# main()

