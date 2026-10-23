from datetime import datetime
from tkinter import *
from tkinter import filedialog as fd
import os


window = Tk()
window.withdraw()

direct = fd.askdirectory()

if direct:
    for file in os.listdir(direct):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            filepath = os.path.join(direct, file)
            lt = os.path.getmtime(filepath)
            ft = datetime.fromtimestamp(lt).strftime('%d.%m.%Y')
            print(ft)


window.mainloop()
