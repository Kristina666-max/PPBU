import turtle as t

t.ht()
r = 40 
t.pensize (5)
t.color ('#FFA500')
t.fillcolor ('#A200FF')
for j in range (4):
    for i in range (6):
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)
    r = r - 10
