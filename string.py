# String in python
# *************************************
'''
    they are surrounded by ' and "

    they are array of byte representing unicode characters.
'''

a = "This is a string."
# *************************************
# looping through a string
for i in a:
    print(i)
'''
    output: 
        T
        h
        i
        s
         
        i
        s
         
        a
         
        s
        t
        r
        i
        n
        g
        .
'''
# *************************************
# size of string - len()
print("lenght of string:",len(a))  # o/p -> lenght of string: 17

# *************************************
# checking in string:
print("is" in a) # o/p -> True

# *************************************
# slicing string
'''
    you can return a range of character by using slice.
    
    but we get chara from position 2 to positin 9 (not included).
'''
print(a[2:9]) # o/p -> is is a

# slicing from start
'''
     by leaving out the start index , range of chara will start at the first chara.
     
     but we get chara from first to positin 9 (not included).
'''
print(a[:9]) # o/p -> This is a

# slicing to the end
print(a[5:]) # o/p -> is a string. , we get chara from position 5 to the end.

# Negative index
print(a[-5:-2]) # o/p -> rin   , r->positiion -5 to -2 (not included).


# **************************************************************************
# String Methods.
b = "  van is good"
'''
    1. Modifying String.
        upper() - make string to Uppercase.
        lower() - make string to Lowecase.
        strip() - Remove whitesplaces from the beginning or the end.
        replace() - to replace a string with another.
        
'''
print(a.upper()) # o/p -> THIS IS A STRING.
print(a.lower()) # o/p -> this is a string.
print(b.strip()) # o/p -> van is good
print(a.replace('i','X')) # o/p -> ThXs Xs a strXng.
print(a.split(" ")) # o/p -> ['This', 'is', 'a', 'string.']

# ***************************************************************************

# String Concatenate
'''
    this is combining two strings.
'''
print(a+b) # o/p -> This is a string.  van is good

# ***************************************************************************

# String Format.
'''
    This method takes passed argument ,format them, and place them in the string  where the placeholder {} are. 
'''
age = 36
text = " my name is prithiv and age is {}"
print(text.format(age)) # o/p -> my name is prithiv and age is 36

text = " my name is {0} and age is {1}"
name = "aswanth"
print(text.format(name,age)) # o/p -> my name is aswanth and age is 36