# They are both data structures that can hold a collection of items.






# stack - using list


# Using list Stack works on the principle of LIFO - “Last-in, first-out”
 
stack = ["Amar", "Akbar", "Anthony"] 
stack.append("Ram") # add to back
stack.append("Iqbal") # add to back
print(stack) # ['Amar', 'Akbar', 'Anthony', 'Ram', 'Iqbal']
  
# Removes the last item 
print(stack.pop()) 
  
print(stack) # ['Amar', 'Akbar', 'Anthony', 'Ram']
  
# Removes the last item 
print(stack.pop()) 
  
print(stack) # ['Amar', 'Akbar', 'Anthony']


# Queues


# Queues are collections of items that follow the FIFO - “First-in, first-out” protocol to store and remove data.

# Queue using list 
queue = ["Ashley", "Akbar", "Anthony"] 
queue.append("Ram") # "Ram" first in being added to the back of the list"
queue.append("Iqbal") # "Iqbal" added 2nd to the back
print(queue) # ['Ashley', 'Akbar', 'Anthony', 'Ram', 'Iqbal']
  
# Removes the first item 
print(queue.pop(0)) # removes "Ashley" (index 0) from our list
  
print(queue) # ['Akbar', 'Anthony', 'Ram', 'Iqbal']
  
# Removes the first item 
print(queue.pop(0)) # removes 'Akbar' (index 0) from our updated list
  
print(queue) # ['Anthony', 'Ram', 'Iqbal']





# Stack using deque


# Using Deque In case of stack, list implementation works fine and provides both append() and pop() in O(1) time. 
# When we use deque implementation, we get same time complexity. 
from collections import deque 
queue = deque(["Ram", "Tarun", "Asif", "John"]) 
print(queue) # deque(['Ram', 'Tarun', 'Asif', 'John'])
queue.append("Akbar") # add to back
print(queue) # deque(['Ram', 'Tarun', 'Asif', 'John', 'Akbar'])
queue.append("Birbal") # add to back
print(queue) # deque(['Ram', 'Tarun', 'Asif', 'John', 'Akbar', 'Birbal'])
print(queue.pop()) # remove from back                 
print(queue.pop()) # remove from back                 
print(queue) # deque(['Ram', 'Tarun', 'Asif', 'John'])
