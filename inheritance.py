 # Inheritance Basics
# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>
# Inheritance
'''
    IT allow us to define class that inherit all properties form other class.
    
    Parent class is the class being inherited from, also called base class.
    
    Child class is the class that inherits from another class, also called derived class.
'''

class Person:  # Base class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print("Name:"+self.name+" age:"+str(self.age))


class Student(Person): # Child class
    pass

p1 = Student("Namil",24)
p1.getName()

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>

'''
    When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    
    Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    
    To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''

class Person:  # Base class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print("Name:"+self.name+" age:"+str(self.age))


class Student(Person): # Child class
    def __init__(self):
        print("child") # only this executes




st = Student()

# >>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<>>>>>>>>>>>>>
# super()
'''
    Python also has a super() function that will make the child class inherit 
    all the methods and properties from its parent
'''


class Person:  # Base class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print("Name:"+self.name+" age:"+str(self.age))


class Person1(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        super().getName()

p1=Person1("jiteesh",39)
