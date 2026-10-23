from tkinter import *

def add_item():
    if s.get() == '0':
        l_1.insert(END, e.get())
        e.delete(0, END)
    else:
        l_2.insert(END, e.get())
        e.delete(0, END)

def del_item():
    l_1.delete(ANCHOR)




window = Tk()
s = StringVar(value=0)
f1 = Frame()
f1.pack(side=LEFT)
m1 = Label(f1, text='Имена')
m1.pack()
l_1 = Listbox(f1)
l_1.pack()


f2 = Frame()
f2.pack(side=LEFT)
m2 = Label(f2, text='Телефоны')
m2.pack()
l_2 = Listbox(f2)
l_2.pack()

f3 = Frame()
f3.pack(side=LEFT)
radio1 = Radiobutton(f3, text='Имя', value=0, variable=s)
radio1.pack()
radio2 = Radiobutton(f3, text='Телефон', value=1, variable=s)
radio2.pack()
e = Entry(f3)
e.pack()
b1 = Button(f3, text='Добавить', command=add_item)
b1.pack()
b2 = Button(f3, text='Удалить', command=add_item)
b2.pack()
