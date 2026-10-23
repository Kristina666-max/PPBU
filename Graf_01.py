from tkinter import *
from PIL import Image, ImageTk, ImageGrab
from tkinter import filedialog as fd
from tkinter import messagebox as mb

size1 = 5

def set_size1():
    global size1
    try:
        size2 = int(entry_size1.get())
        if size2 <= 0:
            raise ValueError("Число должно быть больше нуля")
        size1 = size2
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное целое число (больше 0).")
        entry_size1.delete(0, END)
        entry_size1.insert(0, str(size1))

def draw(event):
    global size1
    x1 = event.x - size1
    y1 = event.y - size1
    x2 = event.x + size1
    y2 = event.y + size1
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=pen_color)

def quit():
    window.destroy()

def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось загрузить: {e}")

def save_canvas():
    try:
        file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG files', '*.png')])
        if file_path:
            x = window.winfo_rootx()
            y = window.winfo_rooty()
            x1 = x + 600
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo("Сохранено!", "Изображение успешно сохранено в PNG файл!")
    except Exception as e:
        mb.showerror("Ошибка", f"Не удалось сохранить: {e}")

window = Tk()
window.title("Графический редактор")

pen_color = "red"
canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(window, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

frame_controls = Frame(window)
frame_controls.pack(pady=10)

Label(frame_controls, text="Толщина кисти:").pack(side=LEFT, padx=5)

entry_size1 = Entry(frame_controls, width=5)
entry_size1.pack(side=LEFT, padx=5)
entry_size1.insert(0, str(set_size1))

btn_set_size1 = Button(frame_controls, text="Установить толщину", command=set_size1)
btn_set_size1.pack(side=LEFT, padx=5)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить изображение", command=load_image)
file_menu.add_command(label="Сохранить холст", command=save_canvas)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)

window.mainloop()
