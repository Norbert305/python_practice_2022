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



def concat(name,age):
  
  return f"My name is {name} and I am {age} years old."
  
print(concat("Bert",20))


def find_duplicates(num):

    obj = {}

    for i in range(len(num)):
        key = num[i]

        if key in obj:
                obj[key]+= 1
            
        else:
            obj[key] = 1

        
    answer = []

    for data in obj:
        if obj[data] >= 2:
            answer.append(data)

    return answer

print(find_duplicates([1,2,2,1,3,4,5,5])) # [1,2,5]
        
    