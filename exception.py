#exception handling using try and except
A=list(range(10))
e_count=0
o_count=0
for i in range(20):
    try:
        if A[i]%2==0:
            e_count+=1
        else:
            o_count+=1
    except IndexError:
        print("Index out of order")
        break
print("even no:",e_count)
print("odd no:",o_count)
            


    
