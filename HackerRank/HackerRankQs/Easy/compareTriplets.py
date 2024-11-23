a = [1, 2, 3]
b = [3, 2, 1]

def compareTriplets(a, b):
    aPoints = 0
    bPoints = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            aPoints +=1
        elif a[i]<b[i]:
            bPoints+=1
    return aPoints, bPoints

print(compareTriplets(a,b))




