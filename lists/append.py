




def get_thirty(my_list):

    empty = []

    for i in range(len(my_list)):
        
        if my_list[i] == 30:
            empty.append(my_list[i])

    return empty

print(get_thirty([10,20,30,40,50]))