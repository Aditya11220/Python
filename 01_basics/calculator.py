a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


print("Please Select the operation you want to perform:\n ")

print("1. Add (+)\n")
print("2. Subtract (-)\n")
print("3. Multiply (*)\n")
print("4. Divide (/)\n")

operation = input("Enter the operation you want to perform: ")

while True:
    if operation == '1':
        print("The sum of ", a, " and ", b, " is: ", a + b)
        break
    elif operation == '2':
        print("The difference of ", a, " and ", b, " is: ", a - b)
        break
    elif operation == '3':
        print("The product of ", a, " and ", b, " is: ", a * b)
        break
    elif operation == '4':
        print("The quotient of ", a, " and ", b, " is: ", a / b)
        # One task for you guys to handle the division by zero error.
        break
    else:
        print("Invalid operation. Please select a valid operation.")
        operation = input("Enter the operation you want to perform: ")  