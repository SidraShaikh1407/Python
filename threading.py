#Aim:Write a Programs on Threading using python.
# Branch: Comps
# Year: SE
# Sem: IV
# Subject: Python
# Name: Sidra Shaikh
# UIN: 231P064
# Roll No: 40
# Multitasking using two threads
from threading import *
from time import *
class Theatre:
    # Constructor
    def __init__(self, str):
        self.str=str

    # Method repeat for 5 tickets
    def movieshow(self):
        for i in range(1,6):
            print(self.str,":",i)
            sleep(0.5)

# create two instance to theatre class
obj1=Theatre ("Cut Ticket ")
obj2=Theatre ("Show Chair ")

# create two thread to run movieshow()
t1=Thread(target=obj1.movieshow)
t2=Thread(target=obj2.movieshow)

# run threads
t1.start()
t2.start()
