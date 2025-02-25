def is_even(no):
    if (no % 2 == 0):
        print(f"{no} is even number.")
    else:
        print(f"{no} is odd number.")

no = int(input("Enter Number : "))
is_even(no)
