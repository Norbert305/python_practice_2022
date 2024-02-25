import random
# my array
my_list = [1,2,3,4,5]
# any random number from 1 to 100
random_numbers = random.randint(1,100)
# loop 5 times
for i in range(5):
    my_list.append(random_numbers)
    # append random number 5 times from random_numbers variable to my_list using for loop  

print(my_list)