from tkinter import *

window = Tk()
text = Text(width=30, height=8,bg='black', fg='white')
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

window.mainloop()
