def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def calculator():
    try:
        print("---- Simple Calculator ----")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Choose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", sub(a, b))
        elif choice == '3':
            print("Result:", mul(a, b))
        elif choice == '4':
            print("Result:", div(a, b))
        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter only numbers!")
calculator()

