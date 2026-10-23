import turtle as t


t.speed (0)
t.ht()
r = 20 
t.pensize (4)
t.color ('#FFA500')
t.fillcolor ('#A200FF')
for k in range (3):
    for j in range (4):
        for i in range (6):
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.rt(60)
        r = r - 5
    t.pu ()
    t.fd(80)
    t.pd ()
    r = 20

