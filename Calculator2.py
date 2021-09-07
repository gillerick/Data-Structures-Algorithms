def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1/num2


print(calculator(9, 10, "+"))
# print(__name__)

if __name__ == "__main__":
    print(calculator(4, 5, "+"))
    print(calculator(4, 5, "-"))
    print(calculator(4, 5, "*"))
    print(calculator(4, 5, "/"))
