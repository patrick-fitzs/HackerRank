def miniMaxSum(arr):
    minsum = sum(sorted(arr)[:-1])
    print(minsum)
    maxsum = sum(sorted(arr)[1:])
    print(maxsum)

arr = [1, 3, 5, 7, 9]
miniMaxSum(arr)
