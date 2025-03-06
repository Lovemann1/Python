first_number = int(input("enter first number : "))
op = input("enter operater: like +,-,*,/")
second_number = int(input("enter second number : "))

if op == "+":
    print(first_number+second_number)
if op == "-":
    print(first_number-second_number)
if op == "*":
    print(first_number*second_number)
if op == "/":
    print(first_number/second_number)
else:
    print("invalid oprater")
