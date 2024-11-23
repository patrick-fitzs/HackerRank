# Create a function for adding elements in an array

numList = [1,2,3]

def simpleArraySum(ar):
    totalCount = 0
    for i in ar:
        totalCount += i
    return totalCount

print(simpleArraySum(numList))