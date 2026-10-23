from tkinter import *

window = Tk()
lb = Listbox(width=15, height=7)
lb.pack()

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
for day in days:
    lb.insert(END, day)
    
window.mainloop()
