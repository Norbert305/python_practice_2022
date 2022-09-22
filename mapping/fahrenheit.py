
from unittest import result


my_list = [8,9,10,15,4]

def fahrenheit(value):

    return value * 9/5 + 32

result = list(map(fahrenheit, my_list))


print(result)