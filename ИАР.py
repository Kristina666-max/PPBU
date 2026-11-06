from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_base_label(event=None):
    code = base_combobox.get()
    if code in currencies:
        base_label.config(text=currencies[code][0])


def exchange():
    base_code = base_combobox.get().strip()
    if not base_code:
        mb.showwarning('Внимание', 'Выберите валюту из списка')
        return

    name, coin = currencies[base_code]

    try:
        url = f'https://api.coinlore.net/api/ticker/?id={coin}'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data and 'price_usd' in data[0]:
            exchange_rate = float(data[0]['price_usd'])
            symvol = data[0].get('symvol', base_code)
            mb.showinfo(
                'Курс обмена',
                f'1 {symvol} ({name}) = {exchange_rate:,.2f} USD'
            )
        else:
            mb.showerror('Ошибка', f'Не удалось получить курс для {base_code}')

    except requests.exceptions.RequestException as er:
        mb.showerror('Ошибка сети', str(er))
    except (ValueError, KeyError, IndexError) as er:
        mb.showerror('Ошибка данных', f'Некорректный ответ API: {er}')


currencies = {
    'Bitcoin': ('Bitcoin', '90'),
    'Ethereum': ('Ethereum', '80'),
    'Tether': ('Tether', '518'),
    'Binance Coin': ('Binance Coin', '2710'),
    'XRP': ('XRP', '58'),
    'USD Coin': ('USD Coin', '33285'),
    'Solana': ('Solana', '33439'),
    'TRON': ('TRON', '2713'),
    'Cardano': ('Cardano', '257'),
    'Hyperliquid': ('Hyperliquid', '36456'),
}

root = Tk()
root.title('Курс обмена криптовалют к USD')
root.geometry('360x400')

Label(root, text='Базовая валюта', font=('Arial', 10)).pack(pady=20)
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=5, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label(root, font=('Arial', 12))
base_label.pack(pady=10)

Button(text='Получить курс обмена к USD',
       command=exchange, font=('Arial', 10)).pack(pady=20)

base_combobox.current(0)
update_base_label()

root.mainloop()