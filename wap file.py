file1=open("file1.txt","r")
l_c=0
w_c=0
k=file1.readlines()
for i in k:
    l_c=l_c+1
    words=i.split()
    for j in words:
        w_c=w_c+1
print("no of lines:",l_c, "no of words:",w_c)
    
