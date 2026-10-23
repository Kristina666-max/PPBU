from tkinter import *
from tkinter import filedialog as fd
import os
import shutil


window = Tk()
window.withdraw()

direct = fd.askdirectory(title='Выберите папку для копирования')

if direct:
    new_dir = direct + '_new'
    if not os.path.exists(new_dir):
        try:
            shutil.copytree(direct, new_dir)
            print(f'Все содержимое папки {direct} скопировано в папку {new_dir}')
        except Exception as e:
            print(f'Ошибка при копировании: {e}')
        else:
            print(f'Папка {new_dir} уже существует')
    else:
        print('Папка не была выбрана')

window.mainloop()
