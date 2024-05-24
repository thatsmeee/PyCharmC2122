def divide(a: float, b: float) -> float:
    try:
        division = a / b
        return division
    except ZeroDivisionError as error:
        return f"Division by zero is not allowed. Error: \n{error}"

def isNumber(a):
    if isinstance(a, float):
        return a
    else:
        try:
            return (float(a),)
        except BaseException as error:
            return False

def numberOperation(symbol: str):
    typeOperation = symbol

    if typeOperation == '+':
        def operation(a: float, b: float) -> float:
            num_a = isNumber(a)
            num_b = isNumber(b)
            if num_a and num_b:
                return num_a[0] + num_b[0]
            else:
                return f'Invalid input: {a}, {b}'
    elif typeOperation == '-':
        def operation(a: float, b: float) -> float:
            return a - b
    elif typeOperation == '*':
        def operation(a: float, b: float) -> float:
            return a * b
    elif typeOperation == '/':
        return divide
    else:
        def operation(a: float, b: float) -> float:
            return f'Operation \"{a} {typeOperation} {b}\" is not realized'

    return operation

#print('Operation +:')
#operation = numberOperation('+')
#result = operation(4, 5)
#print(result)

#print('Operation -:')
#operation = numberOperation('-')
#result = operation(4, 5)
#print(result)

#print('Operation *:')
#operation = numberOperation('*')
#result = operation(4, 5)
#print(result)

#print('Operation /:')
#operation = numberOperation('/')
#result = operation(2, 4)
#print(result)

#print('Operation %:')
#operation = numberOperation('%')
#result = operation(4, 5)
#print(result)

operation = numberOperation(input('Operation symbol: '))
result = operation(4, 5)
print(result)
