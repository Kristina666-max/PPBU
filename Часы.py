from tkinter import *
import time

def tick():
    t = time.strftime('%H:%M:%S')
    m.config(text=t)
    m.after(1000, tick) #рекурсия (функция выводит сама себя)

window = Tk()
m = Label(font='Verdana 24 bold')
m.pack()
tick()
window.mainloop()
