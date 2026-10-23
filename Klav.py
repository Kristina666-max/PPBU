from tkinter import *
import time
from tkinter import messagebox as mb


def load_phrase():
    try:
        with open('phrase.txt') as file:
            return file.read().strip()
    except FileNotFoundError:
        mb.showerror('Ошибка!', 'Файл с фразой не найден')
        return 'quikbrownfow'


def start():
    global i, t
    i = 0
    t = time.time()
    label.config(text=phrase[i])
    window.bind('<Key>', check)


def check(event):
    global i
    if event.char == phrase[i]:
        i += 1
        if i == len(phrase):
            finish()
        else:
            label.config(text=phrase[i])
    else:
        label.config(text=f'Ошибка! Ожидалась буква {phrase[i]},\n нажмите любую клавишу для продолжения')
        window.bind('<Key>', cont)


def finish():
    elapsed = time.time() - t
    time_allowed = len(phrase)
    if elapsed <= time_allowed:
        res = f'Вы победили! Ваше время {elapsed:.1f} сек. Надо было уложиться в {time_allowed} сек.'
        window.unbind('<Key>')
    else:
        res = f'Прошло {elapsed:.1f} сек. Надо было уложиться в {time_allowed} сек.'
        window.unbind('<Key>')
    mb.showinfo('Результат', res)
    if mb.askyesno('Повторить', 'Хотите попробовать еще раз?'):
        start()
    else:
        window.destroy()


    def cont(event):
        global i
        label.config(text=phrase[i])
        window.bind('<Key>', check)

i = 0
t = 0
phrase = load_phrase()


window = Tk()
window.title('Клавиатурный тренажер')
window.geometry('700x100')


label = Label(font=('Helvetica', 24))
label.pack()


start()
window.mainloop()