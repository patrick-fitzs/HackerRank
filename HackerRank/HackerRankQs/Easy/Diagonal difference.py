matrix = [[1,2,3],
          [4,5,6],
          [9,8,9]]

def diagonalDifference(arr):

    n = len(arr)
    first = 0
    second = 0

    for i in range(n):
        first += arr[i][i]
        second += arr[i][n-i-1]

    return abs(first - second)

print(diagonalDifference(matrix))