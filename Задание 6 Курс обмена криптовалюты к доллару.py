from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    base_code_2 = base_combobox_2.get().strip()
    if target_code and base_code and base_code_2:
        try:

            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response_2 = requests.get(f'https://open.er-api.com/v6/latest/{base_code_2}')
            response.raise_for_status()
            response_2.raise_for_status()
            data = response.json()
            data_2 = response_2.json()
            if target_code in data['rates'] and target_code in data_2['rates']:
                exchange_rate = data['rates'][target_code]
                exchange_2_rate = data_2['rates'][target_code]
                base = currencies[base_code]
                base_2 = currencies[base_code_2]
                target = currencies[target_code]
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate:.1f} {target} за 1 {base} и {exchange_2_rate:.1f} {target} за 1 {base_2}')
            else:
                mb.showerror('Ошибка',
                             f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Введите код валюты')


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
