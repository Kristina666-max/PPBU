from tkinter import *


def draw_circle():
    color = color_var.get()
    canvas.create_oval(50,50,150,150, outline=color, fill=color)

def draw_triangle():
    color = color_var.get()
    canvas.create_polygon(50,150,100,50,150,150, outline=color, fill=color)

def draw_square():
    color = color_var.get()
    canvas.create_rectangle(50,50,150,150, outline=color, fill=color)

def clear_canvas():
    canvas.delete('all')
    

window = Tk()
window.title('Рисование фигур')
window.geometry('400x600')
canvas = Canvas(width = 300, height = 200)
canvas.pack()

color_var = StringVar(value='blue')

circle_button = Button(text='Окружность', command=draw_circle)
circle_button.pack(pady=10)

triangle_button = Button(text='Треугольник', command=draw_triangle)
triangle_button.pack(pady=10)

square_button = Button(text='Квадрат', command=draw_square)
square_button.pack(pady=10)

clear_button = Button(text='Очистить', command=clear_canvas)
clear_button.pack(pady=10)

blue_radio = Radiobutton(text='Синий', variable=color_var, value='blue')
blue_radio.pack(pady=10)

red_radio = Radiobutton(text='Красный', variable=color_var, value='red')
red_radio.pack(pady=10)

black_radio = Radiobutton(text='Черный', variable=color_var, value='black')
black_radio.pack(pady=10)


window.mainloop()
