while True:
    try:
        n=int(input("Enter a no:"))
        fh=open("testfile","w")
        fh.write("this is message for exceptional handling")
        sum=0
        for i in range(n+1):
              sum=sum+i
    except IOError:
        print("File Error")
        break
    except ValueError:
        print("Invalid Entry! retry")
    else:
        print("sum is:",sum)
        break
    finally:
        fh.close()
        
    

        
