

def min_max(data):
    
    min = data[0]
    
    max = data[0]
    
    
    for i in range(len(data)):
        if data[i] < min:
            min = data[i]
            
        elif data[i] > max:
            max = data[i]
            
    return [min,max]
    
    
print(min_max([2,1,4,5,3])) # [1,5]


def name_function(names):
    
    if "Bob" in names:
        return True
    else:
        return False    
    
print(name_function(["Norbert", "Bob", "Max", "Sasha"]))