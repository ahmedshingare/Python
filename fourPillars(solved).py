# -------------------four Pillars of OOPS in python -------------------------


# 1 Encapsulation :
print("Encapsulation :")

class Account:
    def __init__(self,balance):        
        self.__balance1 = balance  # //2800

    def deposite(self,amount):
         if amount > 0:
             self.__balance1 += amount  #  2800 + 500
             print("Money Added Successfully")

    def get_balance(self):     
         return self.__balance1
    
Account_Neha = Account(2800)
Account_Neha.deposite(500)
print(Account_Neha.get_balance())


# Solution :  balance1 is public member,so we changed it to __balance1
#             Now, balance is a private variable (__balance), meaning it cannot be accessed directly.

# ------------------------------------------------------------------------------
# 2 Inheritance 

# Single Inheritance :
print("\nSingle Inheritance :")

class Parent:
    def speak(self):
        print("Animal Make A Sound")

class Child(Parent):
    def speak(self):
        super().speak()
        print("Dog is barks")

dog = Child()
dog.speak()
# Solution : speak method defined in parent class was being over ridden in child class, so we use
#            super() to extend the functionality of the parent class instead of completely replacing it.

# Multiple Inheritance :
print("\nMultiple Inheritance :")

class Parent1:
    def func1(self):
        print("This Is From Parent 1")

class Parent2:
    def func2(self):
        print("This is from Parent 2")

class Child(Parent1,Parent2):
    def func3(self):
        print("this Is Child Class")


A = Child()
A.func1()
A.func2()
A.func3()

# 3 Multilevel Inheritance:
#  A   ->  B   -> C
print("\nMultilevel Inheritance :")

class GrandParent:
    def func1(self):
        print("This is GrandParent Class Attributes")

class Parent(GrandParent):
    def func2(self):
        print("This is Parent Class Attributes")

class Child(Parent):
    def func3(self):
        print("This is Child Class")

obj1 = Child()
obj1.func1()
obj1.func2()
obj1.func3()

# Hierachical Inheritance :
print("\nHierarchial Inheritance :")
class Parent:
    def func1(self):
        print("This is Parent Class")

class Child1(Parent):
    def func2(self):
        print("This is Child 1")
        
class Child2(Parent):
    def func3(self):
       print("This is child 2")

A = Child1()
A.func1()
A.func2()

B = Child2()
B.func1()
B.func3()

# Hybrid Inheritance:
print("\nHybrid Inheritance :")

class A:
    def func1(self):
        print("This is A Class")

class B(A):  # Single Inheritance
    def func2(self):
        print("this is B Class")

class C(A):  # Hirarchicle Inheritance 
    def func3(self):
        print("This Is Class C")


class D(B,C):   # Multiple Inheritance
    def func4(self):
        print("This is D Class")

Object = D()
Object.func1() # 1
Object.func2() # 2
Object.func3() # 3
Object.func4() # 4

# --------------------------------------------------------------------------------------------------------

# Polymorphism :
print("\nPolymorphism :")

class Animal:
    def sound(self):
        print("Animal Make Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Meow Meow")

AnimalList  = [Dog(),Cat()]

for animal in AnimalList:
    animal.sound()

# Solution : Animal.sound() is called on the class itself instead of the objects in the list.
#       Replaced Animal.sound() with animal.sound(), Since AnimalList contains instances of Dog and Cat

  
