# calculator
print("enter + for addition")
print("enter - for subtraction")
print("enter x for multiplication")
print("enter / for division")
choice = input("enter your choice: ")
if choice == "+":
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("sum is", a+b)
elif choice == "-":
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("subtraction is", a-b)
elif choice == "x":
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("multiplication is", a*b)
elif choice == "/":
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("division is", a/b)
else:
    print("enter correct choice!!")
