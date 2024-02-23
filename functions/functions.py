def sum(a,b):

    return a + b

answer = sum(5,5)

print(answer)


def loop_this():

    for i in range(5):
        print("Kobe!")

loop_this()

def times_this(a,b):
    return a * b

print(times_this(5,2))



subtract = lambda a,b: a - b

print(subtract(20,10))


def reverse_string(string):
    
    place_holder = ""
    
    string = string.split(' ')
    
    for i in range(len(string)-1,-1,-1):
        place_holder += string[i]
        place_holder += ' '
        
    return place_holder.strip()
    
print(reverse_string("Hello World"))
    