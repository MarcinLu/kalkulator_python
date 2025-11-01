import tkinter as tk
from tkinter import messagebox

# Funkcje matematyczne
def dodaj():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        wynik.set(a + b)
    except ValueError:
        messagebox.showerror("Błąd", "Proszę wpisać prawidłowe liczby!")

def odejmij():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        wynik.set(a - b)
    except ValueError:
        messagebox.showerror("Błąd", "Proszę wpisać prawidłowe liczby!")

def pomnoz():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        wynik.set(a * b)
    except ValueError:
        messagebox.showerror("Błąd", "Proszę wpisać prawidłowe liczby!")

def podziel():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if b == 0:
            messagebox.showerror("Błąd", "Nie można dzielić przez zero!")
        else:
            wynik.set(a / b)
    except ValueError:
        messagebox.showerror("Błąd", "Proszę wpisać prawidłowe liczby!")

def potega():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        wynik.set(a ** b)
    except ValueError:
        messagebox.showerror("Błąd", "Proszę wpisać prawidłowe liczby!")
    except OverflowError:
        messagebox.showerror("Błąd", "Wynik jest zbyt duży!")

# Tworzenie okna
root = tk.Tk()
root.title("Prosty Kalkulator")

# Zmienne
wynik = tk.StringVar()

# Etykiety i pola wejściowe
tk.Label(root, text="Pierwsza liczba:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Druga liczba:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Przycisk do każdej operacji
tk.Button(root, text="Dodaj", width=10, command=dodaj).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Odejmij", width=10, command=odejmij).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Mnożenie", width=10, command=pomnoz).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Dzielenie", width=10, command=podziel).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Potęga", width=10, command=potega).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Pole wyświetlające wynik
tk.Label(root, text="Wynik:").grid(row=5, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=wynik, state="readonly").grid(row=5, column=1, padx=5, pady=5)

# Uruchomienie pętli głównej
root.mainloop()