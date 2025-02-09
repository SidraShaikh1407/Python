# Aim:Write a menu-driven program in Python to implement tuple operations
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No.:40
print("***************************")
print("Tuple Operations")
print("Sidra Shaikh")
print("***************************")

tuple1 = ("Sidra", "Bushra", "Saad", "Sana")
tuple2 = ("Aeroplane", "Boeing", "Aircraft")

while True:
    print("\nMenu:")
    print("1. Create tuple")
    print("2. Display tuple")
    print("3. Find length of tuple")
    print("4. Check if element is present in tuple")
    print("5. Concatenate tuples")
    print("6. Delete tuple")
    print("7. Count occurrences of an element in tuple")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == '1':
        tuple1 = ("Sidra", "Bushra", "Saad", "Sana")
        print("\nTuple created.")
    elif choice == '2':
        print("\nDisplaying the tuple:")
        print(tuple1)
        print("\nIndividual elements:")
        for item in tuple1 :
            print(item)
    elif choice == '3':
        length_of_tuple = len(tuple1)
        print(f"\nLength of the tuple: {length_of_tuple}")
    elif choice == '4':
        element = input("\nEnter the element to check: ")
        if element in tuple1:
            print(f"'{element}' is present in the tuple.")
        else:
            print(f"'{element}' is not present in the tuple.")
    elif choice == '5':
        concatenated_tuple = tuple1 + tuple2
        print("\nConcatenated tuple:")
        print(concatenated_tuple)
    elif choice == '6':
        del tuple1
        print("\nTuple has been deleted.")
    elif choice == '7':
        tuple1 = ("Sidra", "Bushra", "Saad", "Sana")
        element = input("\nEnter the element to count: ")
        count = tuple1.count(element)
        print(f"\n'{element}' appears {count} times in the tuple.")
    elif choice == '8':
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 8.")
