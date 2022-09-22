import random

my_list = [1,2,3,4,5]

random_numbers = random.randint(1,100)

for i in range(5):
    my_list.append(random_numbers)


print(my_list)