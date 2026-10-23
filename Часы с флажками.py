from tkinter import *
import time

def tick():
    t = time.strftime('%H:%M:%S')
    m.config(text=t)
    m.after(1000, tick)

def bg_color():
    m['bg'] = v1.get()

def fg_color():
    m['fg'] = v2.get()

def font():
    m['font'] = v3.get()

def size():
    m['height'] = v4.get()

window = Tk()
m = Label(font='Verdana 16 bold', bg='lightblue', fg='black')
m.pack()


v1 = StringVar()
v1.set('lightblue')
v2 = StringVar()
v2.set('black')
v3 = StringVar()
v3.set('Verdana 16')
v4 = IntVar()
v4.set(1)
c1 = Checkbutton(text='Переключатель цвета фона', variable=v1, onvalue='salmon', offvalue='lightblue', command=bg_color)
c1.pack()
c2 = Checkbutton(text='Переключатель цвета текста', variable=v2, onvalue='white', offvalue='black', command=fg_color)
c2.pack()
c3 = Checkbutton(text='Переключатель шрифта', variable=v3, onvalue='Arial 16', offvalue='Verdana 16', command=font)
c3.pack()
c4 = Checkbutton(text='Переключатель высоты', variable=v4, onvalue=3, offvalue=1, command=size)
c4.pack()



tick()
window.mainloop()
