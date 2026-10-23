from tkinter import *


def calc():
    x = int(e.get())
    y = int(e1.get())
    summ = x + y 
    m.config(text=f"Результат: {summ}")


    
window = Tk()
window.title('Мой калькулятор')
window.geometry('420x320')

m1 = Label(window, text=f'Первое число', font = ('Arial', 10))
m1.pack(pady=15)
e = Entry(window)
e.pack(pady=15)
m2 = Label(window, text=f'Второе число', font = ('Arial', 10))
m2.pack(pady=15)
e1 = Entry(window)
e1.pack(pady=15)
b = Button(window, text='Сложить', command=calc)
b.pack(pady=15)
m = Label(window, text=f'Результат: —', font = ('Arial', 18))
m.pack(pady=15)



window.mainloop()










  
