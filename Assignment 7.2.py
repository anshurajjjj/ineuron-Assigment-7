#Write a menu driven program to perform following operations - Addition, Subtraction,
#Multiplication, Division
print("\nChoose the operation to perform:")
print("1. Addition of two numbers")
print("2. Subtraction of two numbers")
print("3. Multiplication of two numbers")
print("4. Division of two numbers")
print("5. Exit")
choice = int(input("\nEnter your Choice: "))
if choice == 1:
        print("\nAddition of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        c = a+b
        print(c)
if choice == 2:
        print("\nSubtraction of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        d = a-b
        print(d)
if choice == 3:
        print("\nMultiplication of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        e=a*b
        print(e)
if choice == 4:
        print("\nDivision of two numbers")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        f=a/b
        print(f)
elif choice == 5:
        print("Thank You! See you again.")
