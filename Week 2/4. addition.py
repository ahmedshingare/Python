def sum_numbers(a, b):
    sum = a + b
    print(f"sum of {a} and {b} is {sum}")

a = int(input("Enter the first number: "))
b = input("Enter the second number (press Enter to set default value(10)): ")

b = int(b) if b else 10  

sum_numbers(a, b)
