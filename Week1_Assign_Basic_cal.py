# Basic Calculator Program

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation
print("Choose an operation: +, -, *, /")
operation = input("Enter operation: ")

# Perform the operation
if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
