def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

def potega(a, b):
    return a ** b

print("Prosty kalkulator")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")

wybor = input("Wybierz operację (1-5): ")

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

if wybor == "1":
    print("Wynik:", dodaj(a, b))
elif wybor == "2":
    print("Wynik:", odejmij(a, b))
elif wybor == "3":
    print("Wynik:", pomnoz(a, b))
elif wybor == "4":
    print("Wynik:", podziel(a, b))
elif wybor == "5":
    print("Wynik:", potega(a, b))
else:
    print("Nieprawidłowy wybór!")
