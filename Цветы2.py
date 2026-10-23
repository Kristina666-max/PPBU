import turtle as t
import time

t.speed (0)
t.ht()
r = 20 
t.pensize (4)
t.color ('#FFA500')
t.fillcolor ('#A200FF')
for k in range (3):
    print ('___k=' + str (k))
    for j in range (4):
        print ('__j=' + str (j))
        for i in range (6):
            print ('i='+ str (i))
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.rt(60)
            time.sleep (0.1)
        r = r - 5
    t.pu ()
    t.fd(80)
    t.pd ()
    r = 20

