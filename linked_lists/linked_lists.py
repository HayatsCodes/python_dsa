# Linked lists:
# They are simillar to lists but stores data and 
# reference to another element

# Node:
# The element of a linked list.
# in a singly linked list there are 2 different fields:
# 1. Data - contains the value to be stored in the node
# 2. Next - contains a reference to the next node on the list.

# Head: The first node of the linked list and it is required to traverse through the entire lists

# Applications  of linked lists in DSA:
#  Used to implement a queue (FIFO) and stack (LIFO)
#  Used to implement a graph (adjacency lists: a list/dict of linked lists)

# Creating a linked lists with collections.deque

from collections import deque
l_lists = deque('abc')
l_lists.append('d')
l_lists.pop()



