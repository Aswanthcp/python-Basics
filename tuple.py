"""
    TUPLE
"""
#tuple basics
'''
    tuple is used to store multiple data in a single variable.
    it is created using ( )
        1. Ordered
        2. Unchangable
        3. Allow duplicates.
    
    adding and removing of items are possible.
'''

myTuple = ( 1,2,1,4,"A",True)
print(myTuple)

#------------------------------------------------------------------

# adding items
'''
    1. By converting to List.
    2. Adding tuple to another Tuple.
'''
# By converting to List.

y = list(myTuple)
y.append("W")
myTuple = tuple(y)

print(myTuple) # o/p -> (1, 2, 1, 4, 'A', True, 'W')

# Adding tuple to another Tuple.
new_ = (True,"bol")
myTuple += new_
print(myTuple) # o/p -> (1, 2, 1, 4, 'A', True, 'W', True, 'bol')

#---------------------------------------------------------------------------------------------

# Removing items from tuple.
'''
    1. convert to list and remove
    2. delete tuple completely.
'''
# convert to list and remove
y = list(myTuple)
y.remove("W")
myTuple = tuple(y)

print(myTuple) # o/p -> (1, 2, 1, 4, 'A', True, True, 'bol')

# delete tuple completely.
del myTuple
# print(myTuple) # o/p -> NameError: name 'myTuple' is not defined. Did you mean: 'tuple'?

#---------------------------------------------------------------------------------------------
# Unpacking
'''
    it is extracting values back to variables.
'''
fruits = ("apple","banana","orange")
(green,yellow,orange) = fruits
print(green) # o/p --> apple
print(yellow) # o/p -->  banana


#---------------------------------------------------------------------------------------------

# tuple methods
fruits = ("apple","banana","orange","apple")
print(fruits.count("apple")) # o/p --> 2 it gives no of times a specific value occured.
print("index:",fruits.index("banana")) # o/p -> index: 1

#---------------------------------------------------------------------------------------------