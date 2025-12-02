class prime:
    s=0
    e=0
    l=list()
    def __init__(self,a,b):
        self.s=a
        self.e=b
    def getprime(self):
        for i in range(self.s,self.e+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                self.l.append(i)
        return self.l
p=prime(10,20)
mylist=p.getprime()
#print(mylist)
