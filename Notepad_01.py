from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from transliterate import translit, get_available_language_codes
from googletrans import Translator, LANGUAGES


def delete():
    text.delete(1.0, END)
    update_status()

def transliter():
    try:
        source_text = text.get(1.0, END)
        t_text = translit(source_text, 'ru', reversed=True)
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    update_status()

def translate():
    try:
        source_text = text.get(1.0, END)
        translator = Translator()
        t_text = translator.translate(source_text, src='ru', dest='en').text
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    update_status()

def insert():
    try:
        file = fd.askopenfilename()
        if file:
            with open(file, 'r') as f:
                s = f.read()
                text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден.')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    update_status()

def save():
    try:
        file = fd.asksaveasfilename(filetypes=(('TXT files', '*.txt'), ('All files:', '*.*')))

        if file:
            with open(file, 'w') as f:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Файл не найден.')
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка: {e}')

def quit():
    window.destroy()

def update_status():
    content = text.get(1.0, END)
    char_count = len(content)
    word_count = len(content.split())
    status_label.config(text=f'Символов: {char_count} Слов: {word_count}')

window = Tk()

frame = Frame()
frame.pack()

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Открыть', command=insert)
filemenu.add_command(label='Удалить', command=delete)
filemenu.add_command(label='Сохранить', command=save)
filemenu.add_separator()
filemenu.add_command(label='Выход', command=quit)
mainmenu.add_cascade(label='Файл', menu=filemenu)

process_menu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label='Обработка', menu=process_menu)
process_menu.add_command(label='Транслитерация', command=transliter)
process_menu.add_command(label='Перевод на английский', command=translate)

text = Text(frame, width=60, height=20, bg='white', fg='black', wrap=WORD)
text.pack(side=LEFT)
text.bind('<Key>', lambda event: update_status())
scroll = Scrollbar(frame, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

status_label = Label(text='proba', anchor=W)
status_label.pack(fill=X)

update_status()
window.mainloop()