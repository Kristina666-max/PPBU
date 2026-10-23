"""
Нарисуйте семь красных линий. Все они должны быть строго перпендикулярны,
и кроме того, некоторые нужно нарисовать зеленым цветом, а еще некоторые
— прозрачным. Одна из линий должна быть в форме котенка. (Задача повышенной
трудности).

"""

import turtle as t  # Импортируем библиотеку turtle. Будем обрашаться к ней как к t
t.colormode(255)    # Делаем возможным установку цвета RGB
 
r = 40              # Радиусы окружностей
u = 90              # Угол поворота
t.ht()              # Скрываем курсор
t.pensize(5)        # Толщина линии
rgb_red = '#FF0000' # Красный цвет
rgb_grn = '#008000' # Зеленый цвет
rgb_wht = '#FFFFFF' # Белый цвет
clrs = rgb_red

""" Строим красные линии """
t.down()            # Опустить перо
clrs = rgb_red
for i in range(7):
    t.color(clrs)
    t.circle(r, 90, 10)
    t.lt(u)
    r = -r
    u = -u
t.up()

""" Спускаемся вниз на несколько линий """
t.right(90)
t.fd(r*5)
t.right(90)
t.fd(r)

""" Перекрашиваем в зеленые """
r = 40
u = 90
t.down() 
clrs = rgb_grn
for i in range(2):
    t.color(clrs)
    t.circle(r, 90, 10)
    t.lt(u)
    r = -r
    u = -u    
t.up()


""" Перекрашиваем в белый """
r = 40
u = 90
t.down() 
clrs = rgb_grn
for i in range(2):
    t.color(rgb_wht)
    t.circle(r, 90, 10)
    t.lt(u)
    r = -r
    u = -u    
t.up()

""" Создаем котёнка-курсор """
cat_gif = "cat_02.gif"          # Имя файла с картинкой
screen = t.Screen()             # Создаем переменную с картинкой
screen.register_shape(cat_gif)  # Регистрируем форму по имени файла
t = t.Turtle()                  # Создаём черепашку
t.shape(cat_gif)                # Применяем форму к черепашке

""" Проводим линию из котят """
r = 40
u = 90
t.lt(90)
#t.fd(r*6)
t.rt(90)
t.down()
for i in range(2):
    t.stamp()
    t.circle(r, 90, 10)
    t.lt(u)
    r = -r
    u = -u
