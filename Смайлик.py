from tkinter import *

a = 999

def change():
    global a
    a -= 1
    metka['text'] = chr(a)
window = Tk()
metka = Label(text=chr(a), font='Arial 64')
metka.pack()
knopka = Button(text='Следующий смайлик', width = 30, height = 3)
knopka.config(command=change)
knopka.pack()
window.mainloop()
