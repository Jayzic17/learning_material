import sys
import random
import math
import re

# This is a single-line comment

# For more on data structures and algorithms, checkout the Python DSA section on w3schools

"""
This is a
multi-line comment
"""

# General stuff
a = 5							# This is an integer
a += 3							# Adds 3 to the variable a
a1 = None           # This is NULL in python
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
f1 = range(4)         # This creates the list: [0,1,2,3]
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

# Conditions and Loops
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

for i in range(4):
  print(i)

# Functions
def my_function():
	print("hey")
print(my_function())
def my_function2(*args):			# Lets you specify an arbitrary amount of arguments
	print(args[1] + args[2])

# Classes and Objects
class Person:
  def __init__(self, name, age):    #__init__() is the default constructor for every Class in python. Defining it explicitly like this is how you override it
    self.name = name              # self is a reference to the Object itself. It MUST be the 1st parameter whenever you define ANY method in a Class
    self.age = age
  def __str__(self):                #__str__() is the default string representation of the Object in python. Defining it explicitly like this is how you override it
    return self.name + " " + self.age
s = Person("Jonathan", 27)
print(s.name)
print(s.age)

# Linked List
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def findLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
print("The lowest value in the linked list is:", findLowestValue(node1))

node1 = deleteSpecificNode(node1, node4)
traverseAndPrint(node1)

newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)
traverseAndPrint(node1)

# Binary Tree
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ")

def search(node, target):
  if node is None:
    return None
  elif node.data == target:
    return node
  elif target < node.data:
    return search(node.left, target)
  else:
    return search(node.right, target)

def insert(node, data):
  if node is None:
    return TreeNode(data)
  else:
    if data < node.data:
      node.left = insert(node.left, data)
    elif data > node.data:
      node.right = insert(node.right, data)
  return node

def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def delete(node, data):
  if not node:
    return None

  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    # Node with only one child or no child
    if not node.left:
      temp = node.right
      node = None
      return temp
    elif not node.right:
      temp = node.left
      node = None
      return temp

    # Node with two children, get the in-order successor
    node.data = minValueNode(node.right).data
    node.right = delete(node.right, node.data)

  return node

root = TreeNode('1')
nodeA = TreeNode('2')
nodeB = TreeNode('3')
nodeC = TreeNode('4')
nodeD = TreeNode('5')
nodeE = TreeNode('6')
nodeF = TreeNode('7')
nodeG = TreeNode('8')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG

preOrderTraversal(root)
inOrderTraversal(root)
postOrderTraversal(root)
print(search(root, 8))
print(insert(root, 9))
print("\nLowest value:",minValueNode(root).data)
print(delete(root,9))

