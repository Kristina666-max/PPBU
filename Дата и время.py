from tkinter import *
import time

window = Tk()
month = time.strftime('%B')
year = time.strftime('%Y')
day = time.strftime('%d')
match month:
    case 'January':
        month = 'Января'
    case 'February':
        month = 'Февраля'
    case 'March':
        month = 'Марта'
    case 'April':
        month = 'Апреля'
    case 'May':
        month = 'Мая'
    case 'June':
        month = 'Июня'
    case 'July':
        month = 'Июля'
    case 'August':
        month = 'Августа'
    case 'September':
        month = 'Сентября'
    case 'October':
        month = 'Октября'   
    case 'November':
        month = 'Ноября'
    case 'December':
        month = 'Декабря'
        

time = time.strftime('%d, %B, %Y')
m = Label(text=f'{day} {month} {year}', font='Verdana 24 bold')
m.pack()
window.mainloop()
