"""
            LIST
"""
#list basics
a = [1,2,3,4,5,6,7]

'''
    list are used to store multiple items in a single variable.
    
    list are created using '[]' (square brackets).

            1.Ordered  
            2.changable  
            3.allow duplicates
'''
#....................................................................

# accessing list
print("item in index 1:",a[1]) # o/p -> item in index 1: 2

print(a[2:5]) # o/p -> [3, 4, 5]

print("last element:",a[-1]) # o/p -> last element: 7

#....................................................................

# length of list
print("lenght of list:",len(a)) # o/p -> lenght of list: 7

#....................................................................

#list() constructor
'''
    it is used to create a new list.
'''

b = list(('a','b','c'))

print(b) # o/p -> ['a', 'b', 'c']

#....................................................................

# Inserting elements into list.
'''
    1. insert()
    2.append()
    3.extend()
'''

# insert() --> insert items waithout replacing any items, and at a specific index.
b.insert(2,"D")
print(b) # o/p -> ['a', 'b', 'D', 'c']

# append() --> add item in the end
b.append('E')
print(b) # o/p -> ['a', 'b', 'D', 'c', 'E']

# extend() --> append elements from another list.
b.extend(a)
print(b) # o/p -> ['a', 'b', 'D', 'c', 'E', 1, 2, 3, 4, 5, 6, 7]

#....................................................................

# removing elements from list.
'''
    1.remove()
    2.pop()
    3.clear()
    4.del
'''
# remove() --> remove a specified item.
b.remove("D")
print(b) # o/p -> ['a', 'b', 'c', 'E', 1, 2, 3, 4, 5, 6, 7]

# pop() --> remove specified index.
b.pop(3)
print(b) # o/p -> ['a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7]

# clear()  -->  remove all items in the list.
b.clear()
print(b) # o/p -> []

# del --> delete the list completely.
del b
# print(b) # o/p --> NameError: name 'b' is not defined
