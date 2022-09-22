
from operator import countOf


def find_average(my_list):

    counter = 0

    for i in range(len(my_list)):

        counter += my_list[i] / len(my_list)

    return int(counter)    

print(find_average([5,5,5,5]))