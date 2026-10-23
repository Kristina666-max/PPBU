import turtle as t

t.ht ()
r = 40 
t.pensize (8)
for r in range(40, 0, -10):
    for i in range (6):
        t.colormode (255)
        t.color(255, 165, r * 6)
        t.fillcolor (162, r * 6, 255)
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)           
  
