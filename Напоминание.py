from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


window = Tk()
window.title('Напоминание')
label = Label(text='Установите напоминание')
label.pack()
set.button = Button(text='Установить напоминание', command=set)
set.button.pack()


window.mainloop()