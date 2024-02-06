
def min_max(numbers):
    min = numbers[0]
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
        elif numbers[i] < min:
            min = numbers[i]
            
    return [min,max]

print(min_max([2,1,4,5,3]))



def odd_even(num):
    
    answer  = []
    
    for i in range(len(num)):
        if num[i] % 2 == 0:
            answer.append('even')
        else:
            answer.append('odd')
            
    return answer
        
    
print(odd_even([2,2,4,1,1,1,3,4,1,5]))


def even_characters(char):
    
    answer = []
    for i in range(len(char)):
        if i % 2 != 0:
            answer.append(char[i])
            
    return answer
print(even_characters("jkjkjkjk"))


def summation(n):
    counter = 0
    for i in range(1,n+1):
        counter = i + counter
        
    return counter

print(summation(6))


def two_sum(n, target):
    
    for i in range(len(n)-1):
        num1 = n[i]
        for j in range(i + 1,len(n)):
            num2 = n[j]
            if num1 + num2 == target:
                return [num1,num2]
            
    return []
    
print(two_sum([2,3,6,1,8],7))