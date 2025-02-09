# Aim:Write a menu-driven program in Python to implement list operations
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No.:40
print("***************************")
print("Menu-Driven List Operations")
print("Sidra Shaikh")
print("***************************")

# Initial Lists
list1 = ["python", "list", "1974", "2005", "1983"]
list2 = ["Sidra", "Shaikh", "table tennis", "player","2025","February"]

while True:
    print("\nMENU")
    print("1. Create and Display Lists")
    print("2. Find Length of a List")
    print("3. Check if an Element is in the List")
    print("4. Concatenate Two Lists")
    print("5. Replace an Element in a List")
    print("6. Delete an Element from a List")
    print("7. Work with Nested Lists")
    print("8. Exit")
    
    # User choice
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\ni. Create and Display Lists")
        print("list1:", list1)
        print("list2:", list2)
        print("list1[1:4]:", list1[1:4])
        print("list1[1:]:", list1[1:])
        print("list1[0]:", list1[0])
        print("list1 * 2:", list1 * 2)
        print("list1 + list2:", list1 + list2)

    elif choice == "2":
        print("\nii. Find Length of a List")
        print("Length of list1:", len(list1))
        print("Length of list2:", len(list2))

    elif choice == "3":
        print("\niii. Check if an Element is in the List")
        element = input("Enter the element to check: ")
        if element in list1:
            print(f"'{element}' is in list1.")
        else:
            print(f"'{element}' is not in list1.")

    elif choice == "4":
        print("\niv. Concatenate Two Lists")
        result_list = list1 + list2
        print("Result of concatenation:", result_list)

    elif choice == "5":
        print("\nv. Replace an Element in a List")
        print("Original list1:", list1)
        try:
            index = int(input("Enter the index to replace: "))
            new_value = input("Enter the new value: ")
            if 0 <= index < len(list1):
                list1[index] = new_value
                print("Updated list1:", list1)
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input! Please enter a valid index.")

    elif choice == "6":
        print("\nvi. Delete an Element from a List")
        print("Original list1:", list1)
        try:
            index = int(input("Enter the index to delete: "))
            if 0 <= index < len(list1):
                del list1[index]
                print("Updated list1:", list1)
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input! Please enter a valid index.")

    elif choice == "7":
        print("\nvii. Work with Nested Lists")
        books_list = [("C#", 896), ("Java", 750), ("Python", 1269)]
        while True:
            print("\nNested List Operations:")
            print("1. Show Books List")
            print("2. Add a Book")
            print("3. Back to Main Menu")
            nested_choice = input("Enter your choice: ")
            if nested_choice == "1":
                print("\nBook\t\tPrice")
                for book, price in books_list:
                    print(f"{book}\t\t{price}")
            elif nested_choice == "2":
                book_name = input("\nEnter the name of the book: ")
                try:
                    book_price = int(input("Enter its price: "))
                    books_list.append((book_name, book_price))
                    print("Book added successfully!")
                except ValueError:
                    print("Invalid price! Please enter a numeric value.")
            elif nested_choice == "3":
                break
            else:
                print("Invalid choice! Please try again.")

    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
