"""Aim:write an interactive calculator! User input is assumed to be a formula that
consist of a number, an operator (at least + and -), and another number, separated by white
space(e.g. 1 +1).
Split user input using str.split(), and check whether the resulting list is valid:"""
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh 
# UIN:231P064
# Roll No:40
class FormulaError(Exception):
    """Custom exception for invalid formulas"""
    pass

def calculate():
    while True:
        user_input = input("Enter a formula (e.g., 1 + 1) or 'quit' to exit: ").strip()

        if user_input.lower() == 'quit':
            print("Exiting...")
            break

        parts = user_input.split()

        if len(parts) != 3:
            print("Error: Formula must have two numbers and an operator.")
            continue

        try:
            num1 = float(parts[0])
            num2 = float(parts[2])
        except ValueError:
            print("Error: Invalid number input.")
            continue

        if parts[1] not in ['+', '-']:
            print("Error: Invalid operator. Use '+' or '-'.")
            continue

        result = num1 + num2 if parts[1] == '+' else num1 - num2
        print(f"Result: {result}")
        
calculate()
