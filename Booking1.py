from tkinter import *
from tkinter import messagebox as mb

def book_seat(seats):
    s = seat_entry.get()
    try:
        if seats[s] == 'свободно':
            seats[s] = 'забронировано'
            mb.showinfo('Успех', f'Место {s} успешно забронировано.')
        else:
            mb.showinfo('Ошибка',f'Место {s} уже забронировано или не существует.')
    except KeyError:
        mb.showinfo('Ошибка', f'Места {s} не существует.')

def update_canvas()

window = Tk()
window.title('Бронирование мест')
window.geometry('400x200')

canvas = Canvas(width=400, height=200)
canvas.pack(pady=10)

seats = {f"Б{i}": 'свободно' for i in range(1, 10)}
update_canvas()

seat_entry = Entry()
seat_entry.pack(pady=10)

Button(text='Забронировать места', command=book_seat).pack(pady=10)

window.mainloop()
