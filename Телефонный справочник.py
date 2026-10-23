from tkinter import *

def add_item():
    l.insert(END, e.get())
    e.delete(0, END)

def del_item():
    l.delete(ANCHOR)


window = Tk()
l = Listbox()
l.pack(side=LEFT)
f = Frame()
f.pack(side=LEFT)
e = Entry(f)
e.pack()
b1 = Button(f, text='Добавить', command=add_item)
b1.pack()
b2 = Button(f, text='Удалить', command=add_item)
b2.pack()


