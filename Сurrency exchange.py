from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            data = response.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                target_name = currencies[target_code]
                base_name = currencies[base_code]
                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rate:.2f} {target_name} за 1 {base_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")

currencies = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
    "USD": "Американский доллар"
}

window = Tk()
window.title("Курс обмена валюты к доллару")
window.geometry("360x300")

Label(text="Выберите код базовой валюты:").pack(padx=10, pady=10)

base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=10)

Label(text="Выберите код целевой валюты:").pack(padx=10, pady=10)

target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена валют", command=exchange).pack(padx=10, pady=10)

window.mainloop()