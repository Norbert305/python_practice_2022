
# reverse list
my_list = [1,2,3,4,5]
reversed_list = list(reversed(my_list))
print(reversed_list) # [5, 4, 3, 2, 1]

# append list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits) # ['apple', 'banana', 'cherry', 'orange']


# extend list

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]


# remove list

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

# insert list
insert_list = [1,2,3,4,5]
insert_list.insert(0,11)
print(insert_list)  # [11,1,2,3,4,5]

# clear list
clear_list = [1,2,3,4,5]
clear_list.clear()
print(clear_list) # []

# find max number
find_max = [1,2,3,4,5]
max_number = max(find_max)
print(max_number) # 5

# find smallest number
find_min = [1,2,3,4,5]
min_number = min(find_min)
print(min_number) # 1

# sort numbered list
sort_list = [2,1,4,3,5]
sort_list.sort()
print(sort_list)