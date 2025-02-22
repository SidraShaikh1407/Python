# Aim:Write a program to make simple calculator using if statement.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No:40

while True:
    print("\nMENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice >= 1 and choice <= 4:
        print("Enter two numbers: ")
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))

        # Performing the selected operation
        if choice == 1:
            add = n1 + n2
            print("Result = ", add)
        elif choice == 2:
            sub = n1 - n2
            print("Result = ", sub)
        elif choice == 3:
            mul = n1 * n2
            print("Result = ", mul)
        elif choice == 4:
            if n2 != 0:
                div = n1 / n2
                print("Result = ", div)
            else:
                print("Error! Division by zero.")
    elif choice == 5:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Wrong input..!! Please enter a valid choice.")


