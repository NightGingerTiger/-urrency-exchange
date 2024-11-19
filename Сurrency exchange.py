from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_target_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)

def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def update_base_label2(event):
    code = base_combobox2.get()
    name = currencies[code]
    base_label2.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base_code2 = base_combobox2.get()

    if target_code and base_code and base_code2:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            try:
                response2 = requests.get(f'https://open.er-api.com/v6/latest/{base_code2}')
                response2.raise_for_status()

                data = response.json()
                data2 = response2.json()

                if target_code in data['rates']:
                    exchange_rate = data['rates'][target_code]
                    exchange_rate2 = data2['rates'][target_code]
                    target_name = currencies[target_code]
                    base_name = currencies[base_code]
                    base_name2 = currencies[base_code2]
                    mb.showinfo("Курс обмена", f"Курс {exchange_rate:.2f} {target_name} за 1 {base_name}\n"
                                               f"Курс {exchange_rate2:.2f} {target_name} за 1 {base_name2}")
                else:
                    mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
            except Exception as e:
                mb.showerror("Ошибка", f"Ошибка: {e}")
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
window.title("Курсы обмена валюты")
window.geometry("360x350")

Label(text="Выберите код базовой валюты:").pack(padx=5, pady=5)

base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=5, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

base_label = ttk.Label()
base_label.pack(padx=5, pady=5)

Label(text="Выберите код второй базовой валюты:").pack(padx=5, pady=5)

base_combobox2 = ttk.Combobox(values=list(currencies.keys()))
base_combobox2.pack(padx=5, pady=5)
base_combobox2.bind("<<ComboboxSelected>>", update_base_label2)

base_label2 = ttk.Label()
base_label2.pack(padx=5, pady=5)

Label(text="Выберите код целевой валюты:").pack(padx=5, pady=5)

target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=5, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

target_label = ttk.Label()
target_label.pack(padx=5, pady=5)

Button(text="Получить курс обмена валют", command=exchange).pack(padx=5, pady=5)

window.mainloop()