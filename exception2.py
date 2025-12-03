#exception handling to get integer or no only from user.repeat untill user enter no using while loop. 
while True:
    try:
        n=float(input("Enter a no:"))
    except ValueError:
        print("Invalid data! retry and enter number/integer only")
    else:
        break
        
    
