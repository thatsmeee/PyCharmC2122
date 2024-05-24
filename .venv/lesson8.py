from logging import basicConfig, DEBUG, error

basicConfig(level=DEBUG,
            filename='Log.txt',
            filemode='a',
            format='%(levelname)s | %(asctime)s | %(message)s'
            )

def divide(a: float, b: float) -> float:
    try:
        division = a / b
        return division
    except ZeroDivisionError as err:
        error(f"Division by zero is not allowed. Error: {err}")

def isNumber(a):
    if isinstance(a, float):
        return a
    else:
        try:
            return (float(a),)
        except BaseException as ex:
            error(f"Error occurred while converting to float: {ex}")

def arithmetic_operation(symbol: str):
    type_operation = symbol

    if type_operation == '+':
        def operation(a: float, b: float) -> float:
            num_a = isNumber(a)
            num_b = isNumber(b)
            if num_a and num_b:
                return num_a[0] + num_b[0]
            else:
                return f'Invalid input: {a}, {b}'
    elif type_operation == '-':
        def operation(a: float, b: float) -> float:
            num_a = isNumber(a)
            num_b = isNumber(b)
            if num_a and num_b:
                return num_a[0] - num_b[0]
            else:
                return f'Invalid input: {a}, {b}'
    elif type_operation == '*':
        def operation(a: float, b: float) -> float:
            try:
                return a * b
            except Exception as ex:
                error(f"Error occurred while multiplying numbers: {ex}")
    elif type_operation == '/':
        def operation(a: float, b: float) -> float:
            num_a = isNumber(a)
            num_b = isNumber(b)
            if num_a and num_b:
                return divide(num_a[0], num_b[0])
            else:
                return f'Invalid input: {a}, {b}'
    else:
        def operation(a: float, b: float) -> float:
            error(f'Operation \"{a} {type_operation} {b}\" is not realized')
            return None

    return operation

operation_symbol = input('Operation symbol: ')
operation = arithmetic_operation(operation_symbol)
result = operation(4, 0)
print(result)
