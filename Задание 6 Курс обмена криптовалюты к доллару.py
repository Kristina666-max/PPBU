from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def exchange():
    base_code = base_combobox.get().strip()
    coin = currencies[base_code]
    if base_code:
        try:
            url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if coin in data and 'usd' in data[coin] :
                exchange_rate = data[coin]['usd']
                base = base_code
                mb.showinfo('Курс обмена',f'Курс: {exchange_rate:.1f} USD за 1 {base}')
            else:
                mb.showerror('Ошибка',f'Не удалось получить курс для {base_code}')
        except Exception as er:
            mb.showerror('Ошибка', er)


currencies = {
    'Bitcoin': 'bitcoin',
    'Ethereum': 'ethereum',
    'Tether': 'tether',
    'Binance Coin': 'binancecoin',
    'XRP': 'ripple',
    'USD Coin': 'usd-coin',
    'Solana': 'solana',
    'TRON': 'tron',
    'Cardano': 'cardano',
    'Hyperliquid': 'hyperliquid'

}

root = Tk()
root.title('Курс обмена криптовалют к USD')
root.geometry('360x400')

Label(root, text='Базовая валюта').pack(pady=20)
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=5, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label(root, font=('Arial', 12))
base_label.pack(pady=10)

Button(text='Получить курс обмена к USD',
       command=exchange, font=('Arial', 10)).pack(pady=20)


root.mainloop()
