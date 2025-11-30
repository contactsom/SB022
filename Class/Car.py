import sys

class Car:
    pass


obj1=Car()
obj2=obj1
obj3=obj1

print(sys.getrefcount(obj1))



