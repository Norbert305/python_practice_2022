# nested for loop with 2_sum

def two_sum(nums, target):
    
    for i in range(len(nums)-1):
        num1 = nums[i]
        
        for j in range(i + 1,len(nums)):
            num2 = nums[j]
            
            if num1 + num2 == target:
                return [i,j]
            
            
    return []
        
    
    
print(two_sum([1,2,5,8,3],4)) # index 0 and 4


# while loop

i = 1

while i < 6:
    print(i)
    i += 1