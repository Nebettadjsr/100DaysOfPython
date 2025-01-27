# Esay calculater program
# User inputs: Number1, operator, Number 2
# Program output: calculated result
# additional functions: continue calculating with result or restarting/ reseting calculator

import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(art.logo)
    n1 = float(input("What is the first number? "))
    loop = True

    while loop:
        chosen_operater = input("Choose an operator:\n+\n-\n*\n/\nYou choose: ")
        n2 = float(input("What is the second Number? "))
        result = operations[chosen_operater](n1, n2)
        print(f"{n1} {chosen_operater} {n2} = {result}")

        print(f"Dou you want to continue with {result}?\n")
        cont = input("Type (Y)es or (N)o [Start another Calculation] or (C)lose Program: ").lower()

        if cont == "c":
            loop = False
            print("Thank you for using this simple Calculator! =)")
        elif cont == "y":
            n1 = result
        elif cont == "n":
            print("\n" * 25)
            return

calculator()
