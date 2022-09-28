# Datatype in python.

# *************************************
# Numeric datatype

a=10 # integer - <class 'int'>
b=10.12 # float - <class 'float'>
c=10j # complex - <class 'complex'>

# *************************************
# mapping type

d = {"name":"Apple"} # dict - <class 'dict'>
# *************************************
# sequence Type

st="Abcd" # string - <class 'str'>
s = [1,2,3,4] # list -  <class 'list'>
s1 = (1,2,3,4) # tuple - <class 'tuple'>
s2 = {1,2,3,4} # set- <class 'set'>
s3 = range(10) # range-  <class 'range'>
# *************************************
# boolean type

b = True # boolean -  <class 'bool'>

# *************************************

# python casting

'''
    specifying a type on a variable ,this can done using casting.
'''

x = int(20.0) # <class 'int'> here we convert float to int

y = str(10) # <class 'str'> here we convert int to  string.

# *************************************

print(type(y)) # type() is to check  what datatype the given variable is.