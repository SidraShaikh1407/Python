# Aim:Write a menu-driven program in Python to implement Dictionary operations
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No.:40
print("***************************")
print("Dictionary Operations")
print("Sidra Shaikh")
print("***************************")


while True:
    print("\n********** Dictionary Operations Menu **********")
    print("1. Create Dictionary")
    print("2. Access Elements from Dictionary")
    print("3. Change or Add Elements in Dictionary")
    print("4. Delete or Remove Elements from Dictionary")
    print("5. Find Length and Perform Sorting")
    print("6. Exit")
    print("***********************************************")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        dict1 = {}
        print("Empty Dictionary:", dict1)
        dict1 = {1: 'aeroplane', 2: 'Boeing'}
        print("Dictionary with Integer Keys:", dict1)
        dict1 = {'name': 'Sidra', 1: [2, 4, 3]}
        print("Dictionary with Mixed Keys:", dict1)
        dict1 = dict({1:'aeroplane', 2:'Boeing'})
        print("Using dict():", dict1)
        dict1 = dict([(1,'aeroplane'), (2,'Boeing')])
        print("From Sequence as Pairs:", dict1)
    
    elif choice == '2':
        dict1 = {'name':'Sidra', 'age':18}
        print("Dictionary:", dict1)
        print("Access name:", dict1['name'])
        print("Access age:", dict1.get('age'))
    
    elif choice == '3':
        dict1 = {'name':'Sidra', 'age': 18}
        dict1['age'] = 19
        print("Updated Age:", dict1)
        dict1['address'] = 'Mumbai'
        print("After Adding Address:", dict1)
    
    elif choice == '4':
        dict2 = {1:1, 2:8, 3:27, 4:64, 5:125}
        print("Dictionary Before Removal:", dict2)
        print("Popped Element (Key 4):", dict2.pop(4))
        print("Dictionary After pop(4):", dict2)
        print("Popped Arbitrary Item:", dict2.popitem())
        print("Dictionary After popitem():", dict2 )
        del dict2[3]
        print("Dictionary After Deleting Key 3:", dict2)
        dict2.clear()
        print("Dictionary After clear():", dict2)
    
    elif choice == '5':
        dict2= {1: 1, 3: 27, 5:125, 7:256, 9:743}
        print("Length of Dictionary:", len(dict2))
        print("Sorted Keys:", sorted(dict2))
    
    elif choice == '6':
        print("Exiting Program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
