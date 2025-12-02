import pack1.Inheritance1
import sys
sys.path.append(r"C:\Users\Sana Shaikh\Downloads")
import pack1.primeno

x=pack1.Inheritance1.shape(10,15)
print(x.area())
print(x.perimeter())

y=pack1.Inheritance1.box(10,15,20)
print(y.volume())
print(y.perimeter())

p=pack1.primeno.prime(1,20)
print(p.getprime())
