from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk

def quit():
    window.destroy()
    
def open():
    try:
        file = fd.askopenfilename()
        if file:
            img = Image.open(file)
            imgconv = img
            width = int(ws.get())
            heigth = int(hs.get())
            img.thumbnail((width, heigth))
            imgtk = ImageTk.PhotoImage(img)
            img_window = Toplevel(window)
            img_window.title('Просмотр изображения')
            l = Label(img_window, image=imgtk)
            l.pack()
            l.image = imgtk
    except FileNotFoundError:
        mb.showerror('Ошибка!', 'Файл не найден')
    except OSEError:
        mb.showerror('Ошибка!', 'Не удалось открыть файл, возможно это не изображение')       
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка: {e}')



window = Tk()
window.title('Photo')
window.geometry('500x500')

Label(text='Ширина окна').pack()
ws = Spinbox(window, from_=100, to=500, increment=100)
ws.pack()

Label(text='Высота окна').pack()
hs = Spinbox(window, from_=100, to=500, increment=100)
hs.pack()

mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Открыть...', command=open)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=quit)
mainmenu.add_cascade(label='Файл', menu=filemenu)

window.mainloop()


