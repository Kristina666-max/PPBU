from tkinter import *
from tkinter import filedialog as fd
import os
import shutil


window = Tk()
window.withdraw()

direct = fd.askdirectory(title='Выберите папку с изображениями для их копирования')

if direct:
    new_dir = direct + '_new'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    else:
        print(f'Папка {new_dir} уже существует')
    for file in os.listdir(direct):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            sourse_file = os.path.join(direct, file)
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(sourse_file, destination_file)
                print('Файл перемещен')
            except Exception as e:
                print(f'Ошибка перемещения файла {file} : {e}')
    print('Все скопировано')
else:
    print('Папка не была выбрана')


window.mainloop()