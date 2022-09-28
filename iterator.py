# Iterator

'''
    Iterator in Python is simply an object that can be iterated upon.
    An object which will return data, one element at a time.

    Python iterator object must implement two special methods,
        1. __iter__(),
        2. __next__(),
      collectively called the iterator protocol.
'''
# define a list
my_list = [1,2,3,4]
print(dir(my_list))
my_iter = my_list.__iter__()

print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())

