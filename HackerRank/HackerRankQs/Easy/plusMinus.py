def plusMinus(arr):
    minus = 0
    zero = 0
    plus = 0
    n = len(arr)

    for num in arr:
        if num > 0:
            plus += 1
        elif num < 0:
            minus += 1
        else:
            zero += 1

    # Print the results as required
    print(round(plus / n, 6))
    print(round(minus / n, 6))
    print(round(zero / n, 6))

# Example usage:
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)

