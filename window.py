from tkinter import *

def read():
    name = e.get()
    print(name)
    sity = e2.get()
    print(sity)
    

window = Tk()
f1 = Frame()
f1.pack()
f2 = Frame()
f2.pack()
m = Label(f1, text='Введите имя:', bg='gray', fg='white', font='Courier 18 bold')
m.pack(side=LEFT)
m = Label(f2, text='Введите город:', bg='gray', fg='white', font='Courier 18 bold')
m.pack(side=LEFT)
e = Entry(width=50, justify='center', bg='gray', fg='white', font='Courier 18 bold')
e.pack()
e2 = Entry(width=50, justify='center', bg='gray', fg='white', font='Courier 18 bold')
e2.pack()
b = Button(f1, text='Ввод:', bg='gray', fg='white', font='Courier 18 bold', command=read)
b.pack(side=RIGHT)
b2 = Button(f2, text='Ввод2:', bg='gray', fg='white', font='Courier 18 bold', command=read)
b2.pack(side=RIGHT)
window.mainloop()
