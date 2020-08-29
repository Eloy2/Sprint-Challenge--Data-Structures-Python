import time

start_time = time.time()

f = open('C:/Users/Eloy D. Gutierrez/Desktop/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('C:/Users/Eloy D. Gutierrez/Desktop/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
#################################################################################################################### CLEAN FOR LOOP
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)
#################################################################################################################### CLEAN FOR LOOP

# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value): # DONE
#         # Compare target value to node.value
#         # If value > node.value:
#         if value >= self.value:
#             # Go right
#             # If node.right is None:
#             if self.right is None:
#                 # Create the new node there
#                 self.right = BSTNode(value)
#             else:  # self.right is a BSTNode
#                 # Do the same thing (aka recurse)
#                 # Insert value into node.right
#                 # right_child is a BSTNode, so we can call insert on it
#                 self.right.insert(value)
#         # Else if value < node.value
#         if value < self.value:
#             # Go Left
#             # If node.left is None:
#             if self.left is None:
#                 # Create node
#                 self.left = BSTNode(value)
#             else:
#                 # Do the same thing
#                 # (compare, go left or right)
#                 # Insert value into node.left
#                 self.left.insert(value)

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target): # DONE
#         if target == self.value:
#             return True
#         elif target > self.value:
#             if self.right is None:
#                 return False
#             else:
#                 return self.right.contains(target) # WHY do we need to use return here?
#         elif target < self.value:
#             if self.left is None:
#                 return False
#             else:
#                 return self.left.contains(target) # WHY do we need to use return here?

# BTS = BSTNode(names_1[0])

# for name in names_1:
#     BTS.insert(name)

# for name in names_2:
#     if BTS.contains(name):
#         duplicates.append(name)

#################################################################################################################### STRETCH
name1set = set(names_1)
name2set = set(names_2)
# duplicates.append(name1set.intersection(name2set)) DID NOT WORK

duplicates = [i for i in name1set.intersection(name2set)]  # Return the list of duplicates in this data structure # SHOULD RETURN 64 DUPLICATES
#################################################################################################################### STRETCH

# ORIGINAL RUNTIME: 4.3 seconds
# CLEAN FOR LOOP RUNTIME: 1.06 seconds
# BTS RUNTIME: 0.070 seconds
# SET INTERSECTION RUNTIME: 0.0039 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
