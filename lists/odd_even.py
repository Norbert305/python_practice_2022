

def odd_even(my_list):

    x = []

    for i in range(len(my_list)):

        if my_list[i] % 2 != 0:

            x.append(my_list[i])

    return x

print(odd_even([2,4,6,8, 11]))