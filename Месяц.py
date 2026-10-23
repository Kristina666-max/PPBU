import datetime

t = datetime.date.today()
ru = ''
m = t.month  #Храним номер месяца в m
#date = t.strftime('%d %B %Y')
print(f'Текущая дата: {m}')

if m == 1:
    ru = 'января'
elif m == 2:
    ru = 'Февраля'
elif m == 3:
    ru = 'марта'
elif m == 4:
    ru = 'апреля'
elif m == 5:
    ru = 'мая'
elif m == 6:
    ru = 'июня'
elif m == 7:
    ru = 'июля'
elif m == 8:
    ru = 'августа'
elif m == 9:
    ru = 'сентября'
elif m == 10:
    ru = 'октября'
elif m == 11:
    ru = 'ноября'
elif m == 12:
    ru = 'декабря'

print(f'Сегодня {t.day} {ru} {t.year} года.')
