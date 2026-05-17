# Simple Calculator using Python Basics

# Calculator Title
print("===================================")
print("       SIMPLE PYTHON CALCULATOR")
print("===================================")

# List of operations
operations = ["Addition", "Subtraction", "Multiplication", "Division"]

# Tuple for symbols
symbols = ("+", "-", "*", "/")

# Dictionary to map choices
operation_dict = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division"
}

# Display operations using list and index
print("\nAvailable Operations:")

for i in range(len(operations)):
    print(i + 1, ".", operations[i], symbols[i])

# User input
choice = int(input("\nEnter your choice (1-4): "))

# Check valid choice
if choice >= 1 and choice <= 4:

    # Input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculations
    if choice == 1:
        result = num1 + num2

    elif choice == 2:
        result = num1 - num2

    elif choice == 3:
        result = num1 * num2

    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero is not allowed."

    # Print selected operation using dictionary
    print("\nSelected Operation:", operation_dict[choice])

    # Print result
    print("Result:", result)

else:
    print("Invalid Choice! Please select between 1 and 4.")

print("\nThank you for using the calculator!")