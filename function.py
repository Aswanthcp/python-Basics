# function
"""
    definition:
        A function is a block of code which only runs when it is called.

        You can pass data, known as parameters, into a function.

        A function can return data as a result.

"""
def myFunction():
    print("\nhello world!")

myFunction()

# *****************************************************************
# argument/parametrized function
'''
    Information can be passed into functions as arguments.
    Arguments are specified after the function name, inside the parentheses. 
    You can add as many arguments as you want, just separate them with a comma.
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
# *****************************************************************
# arbitary functions
'''
    If you do not know how many arguments that will be passed into your function,
     add a * before the parameter name in the function definition.

'''

def myfun(*kids):
    print("\narbitary argumnt:")
    for i in kids:
        print(i)

myfun("arathi","arjun","banjmin")

# *****************************************************************

# keyword argument
'''
    You can also send arguments with the key = value syntax.
'''
def kargfun(child1,child2):
    print("\nkeyword arg:")
    print(child1+" & "+child2)


kargfun(child1="aswanth",child2="sayanth")

# *****************************************************************
# Arbitrary keyword argument
'''
    If you do not know how many keyword arguments that will be passed into your function,
     add two asterisk: ** before the parameter name in the function definition.
'''
def arbkeyargs(**kwargs):
    print("\narbitary keyword arg:")
    for i in kwargs:
        print(kwargs[i])

arbkeyargs(child1="aswanth", child2="sayanth", child3="divya")

# *****************************************************************
# Defualt
'''
    If we call the function without argument, it uses the default value
'''
print("\n Defualt: arg:")
def defualtfun(value=" defualt function"):
    print("this is a"+value)

defualtfun()

# *****************************************************************
# recursion in function

'''
    Python also accepts function recursion, which means a defined function can call itself.
'''

def recursionfun(k):
    if k>0:
        result = k + recursionfun(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\n recursion example")
recursionfun(6)
# *****************************************************************

# lambda function
'''
    A lambda function is a small anonymous function.
    
    A lambda function can take any number of arguments, but can only have one expression.

'''


print("\n lambda function:")
x = lambda x:x+10

print(x(5))

# *************************************************************************