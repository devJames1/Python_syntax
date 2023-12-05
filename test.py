#!/usr/bin/env python


#print ("Hello, World!")

# word = 'word' #word comment
# print (word)

# '''
# sentence = "This is a sentence."
# print (sentence)
# '''


# paragraph = """This is a paragraph. It is
# made up of multiple lines and sentences"""
# print (paragraph)

# import sys; x = 'foo'; sys.stdout.write(x + '\n');

#############################
# 1.Primitive Datatypes and Operators
###############################

# numbers
3 # => 3

# Math is what you would expect
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Integer division rounds down for both positive and negattive numbers.
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0 # works on floats too
-5.0 // 3.0  # => -2.0
# print (5 // 3, -5 // 3, 5.1 // 3)

# The result of division is always a float
10.0 / 3  # => 3.3333333333333335

# print (10 / 3)

# Modulo operation
# 7 % 3   # => 1
# # i % j have the same sign as j, unlike C
# -7 % 3  # => 2
#In Python unlike C or javascript The negative modulo takes sign of the divisor not the dividend and output remainder will be the number left to add to the  calculated remainder to make the division even 
# print(-7 % 3)

# Exponentiation (x**y, x to the yth power)
2**3  # => 8
# print(3**3)

1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8
# print((1+3 *2), ((1 + 3) * 2))

# Boolean values are primitives (Note: the capitalization)
True   # => True
False  # => False
# print(True, False)

# negate with not
not True   # => False
not False  # => True
# print(not True, not False)

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True
# print(True and False)
# print(False or True)

# True and False are actually 1 and 0 but with different keywords
True + True # => 2
True * 8    # => 8
False - 5   # => -5
# print((True + True), (True * 8), (False - 5))

# Comparison operators look at the numerical value of True and False
0 == False  # => True
2 > True    # => True
2 == True   # => False
-5 != False # => True
# print((0 == False, 2 > True, 2 == True, -5 != False ))

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0)     # => False
bool("")    # => False
bool([])    # => False
bool({})    # => False
bool(())    # => False
bool(set()) # => False
bool(4)     # => True
bool(-6)    # => True

# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
bool(0)     # => False
bool(2)     # => True
0 and 2     # => 0
bool(-5)    # => True
bool(2)     # => True
-5 or 0     # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False
# print(1 == 1, 2 == 1)

# Inequality is !=
1 != 1  # => False
2 != 1  # => True
# print(1 != 1, 2 != 1)

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal
# print(b == a, b is a, )

# Strings are created with " or '
str1 = "This is a string."
str2 = 'This is also a string.'
# print(str1, str2)

# Strings can be added too
c = "off topic"
a = "Hello " + "world! "  + c# => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
b = "Hello " "world! " "extra extra " + c  # => "Hello world!"
# print(a)
# print(b)

# A string can be treated like a list of characters
"Hello world!"[0]  # => 'H'
# print("Hello world!"[2])

# You can find the length of a string
# print(len("This is a string"))  # => 16


# Since Python 3.6, you can use f-strings or formatted string literals.
name = "Reiko"
f"She said her name is {name}." # => "She said her name is Reiko"
# Any valid Python expression inside these braces is returned to the string.
f"{name} is {len(name)} characters long." # => "Reiko is 5 characters long."

# print(f"She said her name is {name}")
# print(f"{name} is {len(name)} characters long")

# None is an object
None  # => None
# print(None);

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
# "etc" is None  # => False
# None is None   # => True



#########################################
## 2. Variables and Collections
#########################################

# Python has a print function
# print("I'm Python. Nice to meet you!") # => I'm Python. Nice to meet you!


# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
# print("Hello, World", end="!") # => Hello, World!

# Simple way to get input data from console
# input_string_var = input("Enter some data: ")
# print("here is your input: " + input_string_var)
# print(f"here is your input: {input_string_var}")

# There are no declarations, only assignments.
# Convention is to use lower_case_with_underscores
some_var = 5
# print(some_var)

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# print(some_unknown_var)

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
# print("yay!" if 0 > 1 else "nay!") # => "nay!"


# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]
# print(other_li)

# Add stuff to the end of a list with append
# li.append(1) # li is now [1]
# print(li)
# li.append(2) # li is now [1, 2]
# print(li)
# li.append(4) # li is now [1, 2, 4]
# print(li)
# li.append(3) # li is now [1, 2, 4, 3]
# print(li)

# Remove from the end with pop
# print("pop last member")
# li.pop()
# print(li)
# print("Let's put it back")
# li.append(3)
# print(li)


# # Access a list like you would any array
# print(li[0]) # => 1
# # Look at the last element
# print(li[-1])


# # Looking out of bounds is an IndexError
# print(li[4]) # Raises an IndexError

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
# print(li[1:3])   # Return list from index 1 to 3 => [2, 4]
# print(li[2:])    # Return list starting from index 2 => [4, 3]
# print(li[:3])   # Return list from beginning until index 3  => [1, 2, 4]
# print(li[::2])  # Return list selecting elements with a step size of 2 => [1, 4]
# print(li[::-1])  # Return list in reverse order => [3, 4, 2, 1]

# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:]
# print(li2)
# print(li is li2) #false

# Remove arbitrary elements from a list with "del"
# del li[2]
# print(li) # li is now [1, 2, 3]

# Remove first occurrence of a value
# li.remove(2)
# print(li)  # li is now [1, 3]
# li.remove(2) # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
# li.insert(1, 2) #li.insert(index, element)
# print("insert 2 back at index 1")
# print(li)

# Get the index of the first item found matching the argument
# print(li.index(2))
# print(li.index(4)) # Raises a ValueError as 4 is not in the list


# You can add lists
# Note: values for li and for other_li are not modified.
# print(li + other_li) # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
# li.extend(other_li)  
# print(li)

# Check for existence in a list with "in"
# print(1 in li)

# Examine the length with "len()"
# print(len(li))

# Tuples are like lists but are immutable.
# tup = (1, 2, 3)
# print(tup[0])  # => 1
# tup[0] = 3 # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
# print(type((1)))
# print(type((1,)))
# print(type(()))

# You can do most of the list operations on tuples too
# print(len(tup))
# print(tup + (4, 5, 6))
# print(tup[:2])
# print(2 in tup) 

# You can unpack tuples (or lists) into variables
# a, b , c = (1, 2, 3) 
# print(a, b, c)

# You can also do extended unpacking
# a, *b, c = (1, 2, 3, 4, 5, 6) 
# print(a, b, c)

# Tuples are created by default if you leave out the parentheses
# d, e, f = 4, 5, 6,
# print(d, e, f)

# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
# e, d = d, e
# print(f"e= {e}, d= {d}")


# Dictonaries store mappings from keys to values

empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}
# print(filled_dict)

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
# invalid_dict = {[1,2,3]: "123"}
# print(invalid_dict) # => Yield a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3): [1,2,3,4]} # Values can be of any type, however.
# print(valid_dict) 

# Look up values with []
# print(filled_dict["one"]) # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - for Python
# versions <3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
# print(list(filled_dict.keys()))  # => ["three", "two", "one"] in Python <3.7
 # => ["one", "two", "three"] in Python 3.7+

 # Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
# print(list(filled_dict.values())) # => [3, 2, 1]  in Python <3.7
# => [1, 2, 3] in Python 3.7+

# Check for existence of keys in a dictionary with "in"
# print("one" in filled_dict) # => True
# print(1 in filled_dict) # => False

# Looking up a non-existing key is a KeyError
# print(filled_dict["four"]) #keyError

# Use "get()" method to avoid the KeyError
# print(filled_dict.get("one")) # => 1
# print(filled_dict.get("four")) # => None
# The get method supports a default argument when the value is missing
# print(filled_dict.get("one", 4)) # => 1
# print(filled_dict.get("four", 4)) # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
# filled_dict.setdefault("five", 5) # filled_dict["five"] is set to 5
# print(filled_dict) 
# filled_dict.setdefault("five", 6) # filled_dict["five"] is still 5
# print(filled_dict) 

# Adding to a dictionary
# filled_dict.update({"four": 4, "seven": 7})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
# print(filled_dict) 
# filled_dict["eight"] = 5
# print(filled_dict)

# Remove keys from a dictionary with del
del filled_dict["one"] 
# print(filled_dict) # Removes the key "one" from filled dict {'two': 2, 'three': 3}

# From Python 3.5 you can also use the additional unpacking options
# print({"a" : 1, **{"b": 2}}) # => {'a': 1, 'b': 2}
# print({"a" : 1, **{"a": 2}}) # => {'a': 2}



# Sets store ... well sets
empty_set = set()
# print(empty_set)
# Initialize a set with a bunch of values.
some_set = {1, 1, 2, 2, 3, 4} # some_set is now {1, 2, 3, 4}
# print(some_set)

# Similar to keys of a dictionary, elements of a set have to be immutable.
# invalid_set = {[1], 1}
# print(invalid_set)
valid_set = {(1,), 1}
# print(valid_set)

# Add one more item to the set
filled_set = some_set
filled_set.add(5) # filled_set is now {1, 2, 3, 4, 5}
# print(filled_set)
# Sets do not have duplicate elements
filled_set.add(5)
# print(filled_set) # it remains as before {1, 2, 3, 4, 5}

# Do set intersection with &
other_set = {3, 4, 5, 6}
# print(filled_set & other_set) # => {3, 4, 5}

# Do set union with |
# print(filled_set | other_set) # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
# print({1, 2, 3, 4} - {2, 3, 5}) # => {1, 4}

# Do set symmetric difference with ^
# print({1, 2, 3, 4} ^ {2, 3, 5}) # => {1, 4, 5}

# Check if set on the left is a superset of set on the right
# print({1, 2} >= {1, 2, 3})

# Check if set on the left is a subset of set on the right
# print({1, 2} <= {1, 2, 3})

# Check for existence in a set with in
# print(2 in filled_set) 
# print(10 in filled_set) 

# Make a one layer deep copy
filled_set = some_set.copy() # filled_set is {1, 2, 3, 4, 5}
# print(filled_set)
# print(filled_set is some_set)



########################################
## 3. Control Flow and Iterables
########################################

# Let's just make a variable
# some_var = 5

# # Here is an if statement. Indentation is significant in Python!
# # Convention is to use four spaces, not tabs.
# # This prints "some_var is smaller than 10"
# if some_var > 10:
#     print("some_var is totally bigger than 10")
# elif some_var < 10: # This elif clause is optional.
#     print("some_var is smaller than 10")
# else:   # This is optional too.
#     print("some_var is indeed 10")


"""
For loops iterate over lists
prints:
    dog is mammal
    cat is a mammal
    mouse is a mammal
"""

# for animal in ["dog", "cat", "mouse"]:
#     # You can use format() to interpolate formatted strings
#     print(f"{animal} is a mammal")

"""
"range(number)" returns an iterable of numbers
from zero up to (but excluding) the given number prints:
    0
    1
    2
    3
"""
# for i in range(4):
#     print(i)

"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
    prints:
        4
        5
        6
        7
"""
# for i in range(4, 8):
#     print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower yo upper number, while incrementing
by step. If step is not indicated, the default
value is 1.
prints:
    4
    6
"""
# for i in range(4, 8, 2):
#     print(i)

"""
loop over a list to retrieve both the index and 
the value of each list item:
    0 dog
    1 cat
    2 mouse
"""
# animals = ["dog", "cat", "mouse"]
# for i, value in enumerate(animals):
#     print(i, value)

"""
While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
# x = 0
# while x < 4:
#     print(x)
#     x += 1  # Shorthand for x = x + 1


# Handle exceptions with a try/except block
# try:
#     # Use "raise" to raise an error
#     # raise IndexError("This is an index error")
#     # print("start") No error raised
# except Exception as e:
#     pass     # Refrain from this, provide a recovery (next example).
# except(TypeError, NameError):
#     pass  # Multiple exceptions can be processed jointly.
# else:   # Optional clause to the try/except block. Must follow # all except blocks.
#     print("All good!")   # Runs only if the code in try raises no exceptions
# finally: # Execute under all circumstances
#     print("We can clean up resources here")


# Instead of try/finally to cleanup resources you can use a with statement
# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="\0")


# Here's an example that demonstrates how the with 
# statement can be used for file handling:
# try:
#     with open("myfile.txt") as f:
#         for line in f:
#             print(line)
# except FileNotFoundError:
#     print("File not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

"""
In this example, the with statement is used to open the file, and if an exception (such as FileNotFoundError) occurs within the block, it will be caught by the subsequent except block.

So, to answer your question, the with statement is not a direct replacement for try/except blocks, but it's often used in combination with them for resource management, providing a cleaner and more Pythonic way to handle resources like files.

"""

# Writing to a file
# contents = {"aa": 12, "bb": 21}
# with open("myfile.txt", "w+") as file:
#     file.write(str(contents))  # writes a string to a file

import json
# contents = {"aa": 12, "bb": 21}
# with open("myfile2.txt", "w+") as file:
#     file.write(json.dumps(contents)) # writes an object to a file

# Reading from a file
# with open("myfile.txt", "r+") as file:
#     contents = file.read() # reads a string from a file
# print(contents)   #{'aa': 12, 'bb': 21}

# with open("myfile2.txt", "r+") as file:
#     contents = json.load(file)  # reads a json object from a file
# print(contents) # print: {"aa": 12, "bb": 21}


# Python offers a fundamental abstraction called the Iterable.
# An iterable is an object that can be treated as a sequence.
# The object returned by the range function, is an iterable.

filled_dict2 = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict2.keys()
# print(our_iterable) # => dict_keys(['one', 'two', 'three']). This is an object
# that implements our Iterable interface.

# We can loop over it.
# for i in our_iterable:
    # print(i) # Prints one, two, three

# However we cannot address elements by index.
# print(our_iterable[1]) # Raises a TypeError

# An iterable is an object that knows how to create an iterator.

# our_iterator = iter(our_iterable)
# print(our_iterator) #<dict_keyiterator object at 0x0000024BBCE867F0>

# Our iterator is an object that can remember the state as we traverse through
# it. We get the next object with "next()".

# print(next(our_iterator))
# It maintains state as we iterate.
# print(next(our_iterator))  # => "two"
# print(next(our_iterator))  # => "three"

# After the iterator has returned all of its data, it raises a
# StopIteration exception
# next(our_iterator)        # Raises StopIteration

# We can also loop over it, in fact, "for" does this implicitly!
# our_iterator = iter(our_iterable)
# for i in our_iterator:
#     print(i)  # Prints one, two, three

# You can grab all the elements of an iterable or iterator by call of list().
# print(list(our_iterable)) # => Returns ["one", "two", "three"]
# print(list(our_iterator)) # => Returns [] because state is saved, this is if the for loop have been called already on our_iterator




####################################
## 4. Functions
#####################################

# def add(x, y):
#     print("x is {} and y is {}".format(x, y))
#     return x + y  # Return values with a return statement

# # Calling functions with parameters
# add(5, 6) # => prints out "x is 5 and y is 6" and returns 11

# # Another way to call functions is with keyword arguments
# add(y=6, x=5)


# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

# print(varargs(1,"bag", [1,2,3],4)) # => (1, 2, 3)

# You can define functions that take a variable number
# of # keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
# print(keyword_args(foot="Big", loch="ness")) # => {'foot': 'Big', 'loch': 'ness'}

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
# all_the_args(1, 2, a=3, b=4) 

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand args (tuples) and use ** to expand kwargs (dictionaries).

args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}

# all_the_args(*args)  # equivalent: all_the_args(1, 2, 3, 4)
# all_the_args(**kwargs)  # equivalent: all_the_args(a=3, b=4)
# all_the_args(*args, **kwargs) # equivalent: all_the_args(1, 2, 3, 4, a=3, b=4)

# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
# (Note: parenthesis have been excluded but can be included)
# print(swap(4, 5))
# x = 1
# y = 2
# x, y = swap(x, y)   # => x = 2, y = 1
# (x, y) = swap(x,y)  # Again the use of parenthesis is optional.
# print(x, y)

# global scope
x = 5

def set_x(num):
    # local scope begins here
    # local var x not the same as global var x
    x = num  # => 43
    print(x)  # => 43

def set_global_x(num):
    # global indicates that particular var lives in the global scope
    global x
    print(x)    # => 5
    x = num     # global var x is now set to 6
    print(x)    # => 6

# set_x(43)
# set_global_x(6)
"""
prints:
    43
    5
    6
"""


# Python has first class functionsdef
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
# print(add_10(3))

# There are also anonymous functions
# print((lambda x: x > 2)(3)) # => True
# print((lambda x, y: x ** 2 + y ** 2)(2, 1)) # => 5


# There are built-in higher order functions
# print(list(map(add_10, [1, 2, 3, 4]))) #[11, 12, 13, 14]
# print(list(map(max, [1, 2, 3], [4, 2, 1])))  # => [4, 2, 3]

# print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))) # => [6, 7]


# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list (which itself may be nested).
# print([add_10(i) for i in [1, 2, 3]])  # => [11, 12, 13]
# print([x for x in [3, 4, 5, 6, 7] if x > 5]) # => [6, 7]

# You can construct set and dict comprehensions as well.
# print({x for x in 'abcdef' if x not in 'abc'})  # => {'d', 'e', 'f'}
# print({x: x **2 for x in range(5)})  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



###################################
## 5. Modules
###################################

# You can import modules
import math
print(math.sqrt(16))  # => 4.0

# You can get specific functions from a module
