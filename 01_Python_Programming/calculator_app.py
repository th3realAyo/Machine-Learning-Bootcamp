"""
    Mini Project: Simple Console Calculator (Beginner Friendly)
    
    Features:
    - Class based calculator
    - Basic operations
    - Loop for repeated use
    - History stored in a list
    - Save and load history using a text file
    - Simple error handling
    
"""


import contextlib
HISTORY_FILE = "calc_history.txt"


class Calculator:
    def __init__(self):
        self.history = self.load_history()

    def load_history(self):
        data = []
        with contextlib.suppress(FileNotFoundError):
            with open(HISTORY_FILE, "r") as file:
                for line in file:
                    if line := line.strip():
                        data.append(line)
            return data

    def save_history(self):
        with open(HISTORY_FILE, "w") as file:
            for item in self.history:
                file.write(item + "\n")

    def get_number(self, message):
        while True:
            value = input(message)
            try:
                return float(value)
            except ValueError as e:
                print("Enter a valid number", e)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            print("Can't divide by zero.", e)

    def Calculate(self, choice):
        a = self.get_number("Enter first number: ")
        b = self.get_number("Enter second number: ")

        if choice == "1":
            result = self.add(a, b)
            op = "+"
        elif choice == "2":
            result = self.subtract(a, b)
            op = "-"
        elif choice == "3":
            result = self.multiply(a, b)
            op = "*"
        elif choice == "4":
            result = self.divide(a, b)
            op = "/"
        else:
            return

        if result is not None:
            record = f"{a} {op} {b} = {result}"
            print(f"Result: {result}")
            self.history.append(record)

    def show_history(self):
        if not self.history:
            print("No calculations yet!")
            return
        print("\nPrevious Calculations:")
        for item in self.history:
            print(item)


def main():
    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2 Subtract")
        print("3 Multiply")
        print("4 Divide")
        print("5 Show history")
        print("6 Exit")

        choice = input("Chose an option: ")

        if choice in ["1", "2", "3", "4"]:
            calc.Calculate(choice)
        elif choice == "5":
            calc.show_history()
        elif choice == "6":
            calc.show_history()
            print("Goodbye. History Saved!")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()