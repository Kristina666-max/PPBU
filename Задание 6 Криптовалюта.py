from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    if target_code and base_code :
        try:

            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()
            if target_code in data['rates'] :
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate:.1f} {target} за 1 {base} ')
            else:
                mb.showerror('Ошибка',
                             f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Введите код валюты')


currencies = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'USDT': 'Tether',
    'BNB': 'Binance Coin',
    'XRP': 'XRP',
    'USDC': 'USD Coin',
    'SOL': 'Solana',
    'TRX': 'TRON',
    'ADA': 'Cardano',
    'HYPE': 'Hyperliquid'

}

root = Tk()
root.title('Курс обмена криптовалют к USD')
root.geometry('360x400')

Label(root, text='Базовая криптовалюта').pack(pady=10)
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack()
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack(pady=10)

Label(root, text='Целевая валюта').pack(pady=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack(pady=10)

Button(text='Получить курс обмена к USD',
       command=exchange).pack(pady=10)


root.mainloop()
