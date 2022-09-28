"""
     SETS

"""
# set basics

myset = {'a','b','c'}

'''
    1. unordered
    2. Unchangable
    3.unindexed
    
Note: you can add and remove items.
    set is written in { }
    
    set() - can make a set
'''

#________________________________________________
# accessing items in set.

for item in myset:
    print(item)

'''
    o/p -> 
            a
            b
            c
'''
#________________________________________________

# checking items in set.
print("c" in myset) # o/p --> True

#________________________________________________

# adding elements in set
'''
        1. add()
        2. update()

'''

# add()
myset.add("d")
print(myset) # o/p --> {'a', 'd', 'b', 'c'}

# update() --> adding another set to current set.
b = {1,2,3,"A",10.1}
myset.update(b)
print(myset) # o/p --> {1, 'd', 'a', 'c', 2, 'b', 3, 10.1, 'A'}

#____________________________________________________________________________________

# removing items from set
'''
        1.remove()
        2.discard()
        3. pop()
'''

# remove() method --> if item removed doesnt exist, remove() will raise error
myset.remove("A")
#     myset.remove("X") #--> KeyError: 'X'
print(myset) # o/p --> {1, 2, 'c', 3, 'a', 'd', 10.1, 'b'}

# discard() method --> if item removed doesnt exist, discard() will not raise error
myset.discard("d")
print(myset) # o/p --> {1, 2, 3, 10.1, 'b', 'c', 'a'}

# pop() method --> remove an item and returns it.
x = myset.pop()
print(myset)# o/p --> {2, 3, 10.1, 'b', 'c', 'a'}
print(x) # o/p --> 1

#________________________________________________________________________________________________

# tuple methods
'''
    1.  copy()
'''

myset = {1,2,3,4,5}
a = myset.copy()
myset.remove(1)
print(a)
print(myset)


#________________________________________________________________________________________________