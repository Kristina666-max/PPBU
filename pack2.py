from tkinter import *

window = Tk()
frame_top = Frame(window)
frame_top.pack()
frame_bottom = Frame(window)
frame_bottom.pack()

metka = Label (frame_top, text='Метка 1', bg='red')
metka.pack()
metka2 = Label (frame_bottom, text='Метка 2', bg='yellow')
metka2.pack()
metka3 = Label (frame_top, text='Метка 3', bg='green')
metka3.pack()
metka4 = Label (frame_bottom, text='Метка 4', bg='BLUE')
metka4.pack()

window.mainloop()
