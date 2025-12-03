#exception handling using try, except, else.
try:
    fh=open("file1.txt","r")
    fh.write("my name is xyz")
except IOError:
    print("can't find file or read data")
else:
    print("Written content in file successfully")
    fh.close()
