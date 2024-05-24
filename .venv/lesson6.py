class Calculator:
    def str_to_float(self, num_str):
        try:
            result = float(num_str)
        except ValueError:
            result = None
            print("Conversion from string to float failed.")
        finally:
            return result

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = None
            print("Division by zero is not allowed.")
        finally:
            return result

calc = Calculator()

while True:
    num1 = calc.str_to_float(input("Number 1: "))
    num2 = calc.str_to_float(input("Number 2: "))
    action = input("Choose an action exit/add/sub/mul/div: ")
    if action == 'exit':
        break
    elif action == 'add':
        print(calc.addition(num1, num2))
    elif action == 'sub':
        print(calc.subtraction(num1, num2))
    elif action == 'mul':
        print(calc.multiplication(num1, num2))
    elif action == 'div':
        print(calc.division(num1, num2))
    else:
        print("Try again")

