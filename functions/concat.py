# Your code goes here:
def render_person(name, date, color, age, gender):
    return f"{name} is a {age} years old {gender} born in {date} with {color} eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))




def sort_arrays(a,b):
    
    c = a + b
    
    my_list = []
    
    for data in range(len(c)):
        if c[data] != 0:
            my_list.append(c[data])
            
    return sorted(my_list)
    
    
print(sort_arrays([2,3,1,5,0,0,0], [4,10,9,7,8,6]))