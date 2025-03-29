"""Aim:Write a Program in python to demonstrate user defined exception.
(month no.is input 1-12, above 12 is exception)."""
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No:40
# User-defined exception
class InvalidMonthError(Exception):
    pass

def check_month(month):
    if month < 1 or month > 12:
        raise InvalidMonthError("Month must be between 1 and 12.")

try:
    month = int(input("Enter month number (1-12): "))
    check_month(month)
    print(f"Month {month} is valid.")

except InvalidMonthError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Please enter a valid number.")

