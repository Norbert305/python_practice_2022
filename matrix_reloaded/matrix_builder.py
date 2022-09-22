#Import random
import random
#Create the function below:


def matrixBuilder(number):

    matrix = []
    #need empty []
    for i in range(number):
        #job for the 1st loop is to push the random
        #number of []'s into your matrix
        matrix.append([])

        for j in range(number):
            #job for the second loop is to push the value 1 into
            #the child []'s 
            matrix[i].append(1)
        
    return matrix

print(matrixBuilder(random.randint(1,9)))