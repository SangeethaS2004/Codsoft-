def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Invalid operation"

print("Welcome to the Simple Calculator!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation:")
print("add - for addition")
print("subtract - for subtraction")
print("multiply - for multiplication")
print("divide - for division")

operation = input("Enter your choice (add/subtract/multiply/divide): ").lower()

result = calculate(num1, num2, operation)
print(f"The result is: {result}")
