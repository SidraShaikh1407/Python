# Aim:WAP Recursive function to calculate sum of a number from 0 to n.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Sidra Shaikh
# UIN:231P064
# Roll No.:40
def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)
num = int (input("Enter a number:"))
if num < 0:
    print("Enter a positive number")
else:
    print("The sum is",recur_sum(num))
