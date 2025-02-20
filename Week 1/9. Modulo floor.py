num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
if num2 == 0:
    print("Division by zero is not allowed.")
else:
    floor = num1 // num2
    remainder = num1 % num2
    print("Floor division = ",floor)
    print("Modulo = ",remainder)
