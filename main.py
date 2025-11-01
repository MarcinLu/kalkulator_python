import tkinter as tk
from tkinter import messagebox

def dodaj_znak(znak):
    entry_var.set(entry_var.get() + znak)

def oblicz():
    try:
        expr = entry_var.get().replace('×', '*').replace('÷', '/').replace('^', '**')
        wynik = eval(expr)
        entry_var.set(str(wynik))
    except ZeroDivisionError:
        messagebox.showerror("Błąd", "Nie można dzielić przez zero!")
    except Exception:
        messagebox.showerror("Błąd", "Nieprawidłowe wyrażenie!")

def wyczysc():
    entry_var.set("")

root = tk.Tk()
root.title("Kalkulator")
root.geometry("400x500")
root.resizable(True, True)  # można ręcznie zmieniać rozmiar okna

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Lista przycisków
przyciski = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', '.', '^', '+'],
    ['C', '=', '', '']
]

for i, rzad in enumerate(przyciski):
    for j, znak in enumerate(rzad):
        if znak != "":
            cmd = wyczysc if znak == "C" else (oblicz if znak == "=" else lambda z=znak: dodaj_znak(z))
            tk.Button(root, text=znak, font=("Arial", 20), command=cmd).grid(row=i+1, column=j, sticky="nsew", padx=2, pady=2)

# Konfiguracja wag kolumn i wierszy dla skalowania
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):  # 5 wierszy przycisków + wyświetlacz
    root.rowconfigure(i, weight=1)

root.mainloop()
