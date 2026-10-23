from tkinter import *
import random

def move_ball(event):
    key = event.keysym
    x1, y1, x2, y2 = canvas.coords(ball)
    if key == 'Up' and y1 > 0:
        canvas.move(ball, 0, -20)
    elif key == 'Down' and y2 < 300:
        canvas.move(ball, 0, 20)
    elif key == 'Left' and x1 > 0:
        canvas.move(ball, -20, 0)
    elif key == 'Right' and x2 < 400:
        canvas.move(ball, 20, 0)
    check_collision()


def check_collision():
    b = canvas.coords(ball)
    print(b)
    s = canvas.coords(square)
    print(s)
    if b[2] > s[0] and b[0] < s[2] and b[3] > s[1] and b[1] < s[3]:
        if b[0] < s[2]:
            print(f'b[0] < s[2]: {b[0] < s[2]}')
    move_square()
    update_score()


def move_square():
    x1, y1 = random.randint(0, 380), random.randint(0, 280)
    x2, y2 = x1 + 20, y1 + 20
    canvas.coords(square, x1, y1, x2, y2)


window = Tk()
window.title('Игра с шариком')
window.geometry('400x300')

canvas = Canvas(width=400, height=300)
canvas.pack()

ball = canvas.create_oval(180, 180, 220, 220, fill='red')
square = canvas.create_rectangle(150, 150, 170, 170, fill='blue')

score = 0

window.bind('<KeyPress>', move_ball)
window.focus_set()


window.mainloop()