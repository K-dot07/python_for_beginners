# Simple Calculator Program

# Step 1: Ask user for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 2: Show options
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Step 3: Take operation input
choice = input("Enter your choice (1/2/3/4): ")

# Step 4: Perform calculation based on choice
if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    print("Result:", num1 / num2)
else:
    print("Invalid input!")
