def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return "Error: Division by zero."
            result = num1 / num2
        else:
            return "Invalid operator."

        return f"The result is: {result}"
    except ValueError:
        return "Invalid input! Please enter numeric values."

print(calculator())