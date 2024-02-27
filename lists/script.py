


# append --->  takes an item as an argument to add the item to the end of a list.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.append(99) # appends 99 at the end of the list


# remove --> The built-in method .remove() removes an item that’s passed as the argument.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.remove(62) # removes 62 from the list


# pop ---> If no index is provided, it takes the last item from the list. Otherwise, if argument is passed, it removes that index.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.pop() # removes ['g', 'h', 'i']
lst.pop(0) # removes 'abc'