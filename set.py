# Aim:Write a menu-driven program in Python to implement set operations
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No.:40
print("***************************")
print("Set Operations")
print("Sidra Shaikh")
print("***************************")

A, B = set(), set()

while True:
    print("\n********** Set Operations Menu **********")
    print("1. Create Sets")
    print("2. Union, Intersection, Difference, Symmetric Difference")
    print("3. Modify Set")
    print("4. Remove Elements from Set")
    print("5. Use Pop and Clear")
    print("6. Check if an Item Exists in a Set")
    print("7. Exit")
    print("*****************************************")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        A = {0, 2, 4, 6, 8}
        B = {11, 2, 13, 4, 15}
        print("Set A:", A)
        print("Set B:", B)
    
    elif choice == '2':
        print("Union of A and B:", A | B)
        print("Intersection of A and B:", A & B)
        print("Difference of A and B (A - B):", A - B)
        print("Symmetric Difference of A and B:", A ^ B)
    
    elif choice == '3':
        set1 = {1, 3}
        print("Initial Set:", set1)
        set1.add(2)
        print("After Adding 2:", set1)
        set1.update([2, 3, 4])
        print("After Adding Multiple Elements:", set1)
        set1.update([4, 5], {1, 6, 8})
        print("After Adding List and Set:", set1)
    
    elif choice == '4':
        set1 = {1, 3, 4, 5, 6}
        print("Initial Set:", set1)
        set1.discard(4)
        print("After Discarding 4:", set1)
        set1.remove(6)
        print("After Removing 6:", set1)
        set1.discard(2)  # No error if not present
        print("After Discarding 2:", set1)
    
    elif choice == '5':
        set1 = set("HelloWorld")
        print("Initial Set:", set1)
        print("Popped Element:", set1.pop())
        print("Set after pop:", set1)
        set1.clear()
        print("Set after clear:", set1)
    
    elif choice == '6':
        set1 = set("apple")
        print("Set:", set1)
        print("Is 'a' in the set?", 'a' in set1)
        print("Is 'p' not in the set?", 'p' not in set1)
    
    elif choice == '7':
        print("Exiting Program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
