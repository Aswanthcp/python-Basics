# Class and Object  Basics
'''
    Python is an object oriented programming language.
    Almost everything in Python is an object, with its properties and methods.
'''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# class
'''
    A Class is like an object constructor, or a "blueprint" for creating objects.
'''

class MyClass:
    x=10
 # class named MyClass, with a property named x

obj1 = MyClass()  # creating object for class

print("class property:",obj1.x)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# __init__() :
'''
   __init__() is a Build-in function in python.
   All class calls  __init__(),which is always executed when the class is being initiated.
   __init__() is assign defualt values to the object properties.
   Note: The __init__() function is called automatically every time the class is being used to create a new object.
'''
print("\n __int__() basics:")
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = Person("aswanth",12)

print(p1.name)
print(p1.age)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#  __str__()

'''
    to make object representation into string.
'''

print("\n __str__() basics:")
class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}  age:{self.age}"


p1 = Person2("Ajay",23)
print(p1)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Object Methods

print("\n Object Methods")

class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myAge(self):
        print("my age is : "+ str(self.age))


p1 = Person2("aswanth",12)

p1.myAge()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#  deleting object property
print("\n delete Object and object property.")
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p3 = Person3("aswanht",21)
del p3 # DELETING obj
#   print(p3)

del p3.age # object property.
print(p3.age)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# pass

class Person:
    pass

# having an empty class definition like this, would raise an error without the pass statement

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>