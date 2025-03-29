""" Aim:Write a program in Python to Perform following operations on file handling.
1. Reading a file
2. Writing into a file
3. Appending into a file """
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No.:40
def read_file(filename):
    """Reads and displays the content of a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:\n" + content)
    except FileNotFoundError:
        print("\nError: File not found!")


def write_file(filename):
    """Writes user input to a file (overwrites existing content)."""
    text = input("\nEnter text to write into the file: ")
    with open(filename, 'w') as file:
        file.write(text)
    print("\nFile written successfully!")


def append_file(filename):
    """Appends user input to the file without deleting existing content."""
    text = input("\nEnter text to append to the file: ")
    with open(filename, 'a') as file:
        file.write("\n" + text)
    print("\nText appended successfully!")


def main():
    filename = "movies.txt"  # Default filename

    while True:
        print("\nFile Handling Operations:")
        print("1. Read File")
        print("2. Write to File")
        print("3. Append to File")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            read_file(filename)
        elif choice == '2':
            write_file(filename)
        elif choice == '3':
            append_file(filename)
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a valid option.")


if __name__ == "__main__":
    main()
