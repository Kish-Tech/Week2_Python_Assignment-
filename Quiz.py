num1=float(input("Enter the first number"))
num2= float(input("Enter the second number"))
operation=input("Enter an operation(+,-,/,*): ")

#Operation
if operation == "+":
    result= num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} ={result}")
elif operation == "/":
    if num2 == 0:
        print("Error:Division by zero is not allowed")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

else:
    print("Invalid operation! Please insert one of these operations +, -, / or *")
