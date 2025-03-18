operator = input("Enter operator (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")    
elif operator == '/':
    if num2 == 0:
        result = "Error! Division by zero."
    else:
        result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print(f"Invalid operator. Please enter one of the specified operators.")