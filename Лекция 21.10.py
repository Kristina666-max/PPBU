import os.path
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import requests
import os


def get_dog_image(url):
    global image_s
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        return data['message']
    except Exception as err:
        print(f'Ошибка чтения API: {err}')
        return None


def show_image():
    global image_s
    image_url =  get_dog_image('https://dog.ceo/api/breeds/image/random')
    try:
        resp = requests.get(image_url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        image_s = Image.open(image_data)
        image = image_s
        image.thumbnail((688, 480))
        image = ImageTk.PhotoImage(image)
        label.config(image=image)
        label.image=image
    except Exception as err:
        print(f'Ошибка чтения API: {err}')
        return None


def save_image():
    global image_s
    if image_s is None:
        mb.showinfo('Картинка', 'Отсутствие загруженного изображения')
        return None

    def_name = os.path.basename(name_file)
    fp = fd.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG', '*.png'),
                   ('JPEG', '*.jpg'),
                   ('ALL Files', '*.*')],
        initialfile=def_name
    )

    if fp:
        image_s.save(fp)
        mb.showinfo('Save',
                    f'Saved: {fp}')


image_s = ''
name_file = 'image_'
root = Tk()
root.title('Dogs')
root.geometry('620x550')
label = Label(root)
label.pack()

btn = Button(root, text='Загрузить', command=show_image)
btn.pack(pady=5)

save_btn = Button(root, text='Сохранить', command=save_image)
save_btn.pack(pady=5)


show_image()
root.mainloop()