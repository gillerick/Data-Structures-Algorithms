def calculator(a, b, operation):
    a = int(a)
    b = int(b)

    if operation == '+':
        solution = a + b
    elif operation == '-':
        solution = a - b
    elif operation == '*':
        solution = a * b
    elif operation == '/':
        solution = a/b
    else:
        return 'Unknown operation'
    return solution


if __name__ == "__main__":
    print(calculator(2, 4, '+'))
    print(calculator(4, 6, 'j'))
