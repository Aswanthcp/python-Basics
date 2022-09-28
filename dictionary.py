"""
        DICTIONARY
"""

# dictionary basics

mydict = {
    "firstname":"Amal",
    "lastname":"Thomas",
    "age":22
}

'''
        In dictionary, data are stored  in key:value pairs.
            1. Ordered
            2. Changeable
            3. Don't allow duplicate.
            
        duplicate value will overwrite existing values.
'''
# ----------------------------------------------------------------------------------------------------
# len() --> how much items are there in dict.

l = len(mydict)
print(l)

# ----------------------------------------------------------------------------------------------------
# accesing dict items.

'''
    1. using key-names
    2. get()
'''
# using key-name
print(mydict["firstname"])

# using get() method
print(mydict.get("lastname"))

# ----------------------------------------------------------------------------------------------------

# get all keys

print(mydict.keys()) # o/p --> dict_keys(['firstname', 'lastname', 'age'])

# get all values

print(mydict.values())  # o/p --> dict_values(['Amal', 'Thomas', 22])

# get all items

print(mydict.items()) # o/p --> dict_items([('firstname', 'Amal'), ('lastname', 'Thomas'), ('age', 22)])

# ----------------------------------------------------------------------------------------------------
# changing values

'''
    1. using keyname
    2. update() method.
'''
# using keyname
mydict["firstname"] = "Aswanth"
print(mydict) # o/p --> {'firstname': 'Aswanth', 'lastname': 'Thomas', 'age': 22}

# update()
mydict.update({'lastname':'C P'})
print(mydict) # o/p --> {'firstname': 'Aswanth', 'lastname': 'C P', 'age': 22}

# ----------------------------------------------------------------------------------------------------
#  Adding values in dict
'''
     1. adding new  key 
     2 . update()
'''
# adding new key
mydict["color"] = "brown"
print(mydict) # o/p -> {'firstname': 'Aswanth', 'lastname': 'C P', 'age': 22, 'color': 'brown'}

# update()
mydict.update({"designation":"python developer"})
print(mydict) # o/p --> {'firstname': 'Aswanth', 'lastname': 'C P', 'age': 22, 'color': 'brown', 'designation': 'python developer'}

# ---------------------------------------------------------------------------------------------------------------------------------------------
 #removing items in dict
'''
        1. pop()
        2. popitem()
        3. del
        4.clear()
 '''

# pop() ----> remove the item with specified keyword
mydict.pop("designation")
print(mydict) # o/p --> {'firstname': 'Aswanth', 'lastname': 'C P', 'age': 22, 'color': 'brown'}

# popitem() --> remove last inserted items
mydict.popitem()
print(mydict) # o/p --> {'firstname': 'Aswanth', 'lastname': 'C P', 'age': 22}

# clear() --> clear the dictionary
mydict.clear()
print(mydict) #--> {}

# del --> completely deletes the dict
del mydict
# print(mydict) # o/p-error --> NameError: name 'mydict' is not defined

#---------------------------------------------------------------------------------------------------------------------------------------------
