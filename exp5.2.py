""" WAP to create a user-defined exception where the program will ask the user
to input a number again and again until the user enters
the correct stored number."""
# Branch: Comps
# Year: SE
# Sem: IV
# Subject: Python
# Name: Sidra Shaikh
# UIN: 231P064
# Roll No: 40

# User-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

# Define class for NegativeValueError
class NegativeValueError(Error):
    """Raised when the input is negative"""
    pass

# Define class for ValueTooSmallError
class ValueTooSmallError(Error):
    """Raised when the value is too small"""
    pass

# Define class for ValueTooLargeError
class ValueTooLargeError(Error):
    """Raised when the value is too large"""
    pass

# Main program: Takes input until the user inputs the correct value
import random

# Generate a random stored number between 1 and 20
number = random.randint(1, 20)

while True:
    try:
        num = int(input("Enter a number: "))

        if num < 0:
            raise NegativeValueError
        elif num < number:
            raise ValueTooSmallError
        elif num > number:
            raise ValueTooLargeError
        
        break  # Exit loop if the correct number is entered

    except NegativeValueError:
        print("This is a negative value, try again.\n")
    except ValueTooSmallError:
        print("This value is too small, try again.\n")
    except ValueTooLargeError:
        print("This value is too large, try again!\n")
    except ValueError:
        print("Invalid input! Please enter a valid integer.\n")

print("\nCorrect value entered!")
 
