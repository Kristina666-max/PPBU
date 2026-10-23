from tkinter import *

def delete():
    text.delete(1.0, END)
    
def insert():
    pushkin ='Я помню чудное мгновенье: Передо мной явилась ты, \
Как мимолётное виденье, Как гений чистой красоты. \
В томленьях грусти безнадежной, \
В тревогах шумной суеты, Звучал мне долго голос нежный \
И снились милые черты.'
    T = text.insert(1.0, pushkin)
  
window = Tk()
text = Text(width=30, height=8,bg='black', fg='white', wrap=WORD)
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b = Button(text='Вставка текста', command=insert)
b.pack(side=LEFT)
b2 = Button(text='Удаление текста', command=delete)
b2.pack(side=LEFT)

window.mainloop()
