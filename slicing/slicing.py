my_list = [1,2,3,4,5]

print(my_list[ :2]) # [1,2] ---> grabbing the first 2 (length 2)
print(my_list[-1]) # 5 ---> last index of the array
print(my_list[2:-1]) # [3,4] ---> monkey in the middle (index 2 and minus length 1)
print(my_list[-3: ]) # [3,4,5] ---> grabbing the last 3 (length 3)
print(my_list[2: ]) # [3,4,5]  --> everything not counting the first 2 (not grabbing length 2)
print(my_list[ :-4]) # [1] ---> subtract length 4