from tkinter import *

def change():
    metka['text'] = 'Черная метка'
    metka['bg'] = 'black'

window = Tk()
metka = Label(text='Привет, всем!', bg = 'red', fg = 'blue', width=15, height=5)
metka.pack()
knopka = Button(text='Изменить метку', width=20, height=3)
knopka.config(command=change)
knopka.pack()
window.mainloop()
