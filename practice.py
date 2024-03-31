# int findMaxSum (int *inputList)
# {
#     int first = *inputList
#     int second = *(inputList+1)
    

# }

# int *maxPair (int *inputList)
# {

# }

def findMaxSum (inputList):
    maxSum = inputList[0]+inputList[1]
    maxFirst = inputList[0]
    maxSecond = inputList[1]
    for i in range(len(inputList)-1):
        first = inputList[i]
        second = inputList[i+1]
        sum = first+second
        if sum>maxSum:
            maxSum = sum
            maxFirst = first
            maxSecond = second
    return (maxFirst,maxSecond)

def maxPair (inputList):
    return findMaxSum(inputList)


print(maxPair([0, 5, 5, 2]))
print(maxPair([0, 4, 3, 1, 2, 3, 4, 0]))