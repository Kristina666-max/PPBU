from tkinter import *
import tkinterweb 

def read():
    site = e.get()
    frame.load_website('site')
   
window = Tk()
f = Frame()
f.pack()

m = Label(f, text='Введите адрес сайта:')
m.pack(side=LEFT)
e = Entry(f, width=20)
e.pack(side=LEFT)
b = Button(f, text='Ввод', command=read)
b.pack(side=LEFT)

frame = tkinterweb.HtmlFrame(window)
frame.pack(fill='both', expand=1)


window.mainloop()

