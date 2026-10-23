import datetime

t = datetime.date.today()
ru = ''
m = t.month  #Храним номер месяца в m
s = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
month_ru = s[m]

print(f'Сегодня {t.day} {month_ru} {t.year} года.')
