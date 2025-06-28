import sys
import random
import math
import re

# This is a single-line comment

"""
This is a
multi-line comment
"""

# General stuff
a = 5							# This is an integer
a += 3							# Adds 3 to the variable a

b = "Jonathan"					# This is a string
b1 = '5'					# This is also a string
b2 = True						# This is a boolean
b3 = False						# This is a boolean
c = str(a)						# Converts to a string
d = int(b1)						# Converts to an integer
e = float(a)					# Converts to a float

print(type(a))					# Returns the data type
print(b + c)					# Concatinate strings
print(random.randrange(1,10))	# Random number btwn 1 and 10
print(b[0])						# First character of a string
print(b[2:5])					# Third through fith character of string: 'nat'
print(b[:3])					# First 3 characters of string: 'Jon'
print(b[4:])					# Last 4 characters of string: 'than'
print(b[-4:-2])					# Fourth-to-last character to third-to-last: 'th'
print(len(b))					# Length of a string
print("Jon" in b)				# Returns true if a string exists in a string
print("x" not in b)				# Returns true if a string does not exist in a string
print(b.lower())				# Lower case string
print(b.upper())				# Upper case string
print(b.strip())				# Removes leading whitespace
print(b.replace("J", "K"))		# Replaces a string w/ another string
print(b.split("a"))				# Splits string into list given a delimiter
print(10 > 9)
print(10 == 9)
print(10 > 9)
print(10 != 9)
print(10 >= 9)
print(10 <= 9)
print(b2 and b3)
print(b2 or b3)
print(not b2)
print(min(1,2,3))
print(max(1,2,3))
print(abs(-1))
print(pow(2,3))
print(math.sqrt(9))
print(re.search("^Jon", b))		# Returns True if the regex matches the string

# Lists
f = [1, 2, 3]					# This is a list
g = [4, 5, 6]
h = f.copy()					# Creates a copy of list 'f'
i = f + g						# Contatinates lists
f.insert(2, 2.5)				# Inserts value in a list right before specified index
f.append(4)						# Appends value to the end of the list
f.extend(g)						# Appends the list 'g' to the end of list 'f'
f.remove(1)						# Removes the specified value from the list (only the 1st occurence)
f.pop(0)						# Removes the specified index from the list
f.pop()							# Removes the last index from the list
f.sort()						# Sorts the list
f.sort(reverse = True)			# Sorts in descending order
f.clear()						# Clears the entire list

# Sets
j = {1, 2, 3}					# This is a set (duplicates are not allowed)
k = {4, 5, 6}
l = j.union(k)					# Returns the union of 2 sets
m = j | k | l					# Containate multiple sets 
j.add(4)						# Adds a value to the set
j.update(k)						# Adds 2 sets together
j.remove(1)						# Removes a value from the set
j.clear()						# Clears the set

# Dictionaries
n = {							# This is a dictionary (duplicate keys are not allowed)
  "jon": 27,
  "andrew": 28,
  "paige": 21
}
o = n.keys()					# Returns a list of all keys
p = n.values()					# Returns a list of all values
q = n.copy()					# Returns a copy of the dictionary: 'n'
print(n["jon"])					# Returns the value of key: 'jon'
print(n.get("jon"))				# Also returns the value of key: 'jon'
n["jon"] = 28					# Changes value of key: 'jon'
n["mom"] = 57					# Adds a new key/value pair
n.pop("mom")					# Removes the key/value pair with the specified key
n.clear()						# Clears the dictionary

# Loops
if 2 > 1:
  print("2 is greater than 1")
elif 1 > 2:
  print("1 is greater than 2")
else:
  print("2 is equal to 1")

r = 1
while r < 6:
  if r == 3:
  	break						# Exist the loop automatically
  if r == 4:
  	continue					# Immediately stops the current iteration and goes back up to the next iteration
  print(i)
  r += 1

for i in f:
  print(i)

# Functions
def my_function():
	print("hey")
print(my_function())
def my_function2(*args):			# Lets you specify an arbitrary amount of arguments
	print(args[1] + args[2])



