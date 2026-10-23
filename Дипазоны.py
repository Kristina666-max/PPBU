import turtle as t

t.ht()
t.pensize (3)
t.color ('blue')
#t.rt(60)
for i in range (4, 56, 4):
    t.fd(i)
    t.rt(90)
t.lt (90)
for i in range (52, 0, -4):
    t.fd(i)
    t.rt(90)

