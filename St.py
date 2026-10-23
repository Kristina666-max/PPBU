from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image
import stepic


def open_file():
    file = fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp')])
    file_path.set(file)

def encode_text():
    image_path = file_path.get()
    text = text_to_encode.get()
    output_path = 'encoded_image.png'

    try:
        image = Image.open(image_path)
        encoded_image = stepic.encode(image, text.encode())
        encoded_image.save(output_path)
        mb.showinfo('Успешно!', 'Текст успешно зашифрован!')
    except Exception as e:
        mb.showerror('Ошибка!', 'str(e)')

def decode_text():
    image = file_path.get()
    try:
        image = Image.open(image_path)
        decoded_text = stepic.decode(image)
        mb.showinfo('Декодированный текст', decoded_text)
    except Exception as e:
        mb.showerror('Ошибка!', 'str(e)')


window = Tk()

file_path = StringVar()
Label(text='Путь к изображению').pack()
Entry(textvariable=file_path, width=60).pack()
Button(text='Выбрать файл', command=open_file).pack()

text_to_encode = StringVar()
Label(text='Текст для шифрования').pack()
Entry(textvariable=text_to_encode, width=60).pack()

Button(text='Зашифровать текст', command=encode_text).pack()
Button(text='Расшифровать текст', command=decode_text).pack()

window.mainloop()