# main.py - prosty kalkulator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nie można dzielić przez 0!"
    return a / b

def main():
    print("Prosty kalkulator")
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    print("Wybierz operację: +, -, *, /")
    op = input("Operacja: ")

    if op == "+":
        print("Wynik:", add(x, y))
    elif op == "-":
        print("Wynik:", subtract(x, y))
    elif op == "*":
        print("Wynik:", multiply(x, y))
    elif op == "/":
        print("Wynik:", divide(x, y))
    else:
        print("Nieznana operacja!")

if __name__ == "__main__":
    main()