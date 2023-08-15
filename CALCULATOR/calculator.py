# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Enter operation number (1/2/3/4): "))

# Perform the calculation based on the operation chosen
if operation == 1:
    result = num1 + num2
elif operation == 2:
    result = num1 - num2
elif operation == 3:
    result = num1 * num2
elif operation == 4:
    if num2 != 0:  # Avoid division by zero
        result = num1 / num2
    else:
        print("Error: Division by zero")
        result = None
else:
    print("Invalid operation")
    result = None

# Display the result if it's not None
if result is not None:
    print("Result:", result)
