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

print(times_this(5,2)) # 10



subtract = lambda a,b: a - b

print(subtract(20,10)) # 10


def reverse_string(string):
    
    place_holder = ""
    
    string = string.split(' ')
    
    for i in range(len(string)-1,-1,-1):
        place_holder += string[i]
        place_holder += ' '
        
    return place_holder.strip()
    
print(reverse_string("Hello World")) # world hello



def summation(n):
    
    count = 0
    
    for i in range(n+1):
        count += i
    
    return count

print(summation(5)) # 1 + 2 + 3 + 4 + 5


def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1)
   
print(factorial(5)) # 5 * 4 * 3 * 2 * 1
        
    