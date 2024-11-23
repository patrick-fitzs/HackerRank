# Given an array of integers,
# calculate the ratios of its elements that are positive,
# negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.
#
# Note: This challenge introduces precision problems.
# The test cases are scaled to six decimal places,
# though answers with absolute error of up to  are acceptable.
#
# Example
#
# There are  elements, two positive, two negative and one zero. Their ratios are ,  and .
# Results are printed as:
#
# 0.400000
# 0.400000
# 0.200000

numList = [-1,-1,0,1,1]

def plusMinus(arr):
    minus = 0
    plus = 0
    zero = 0
    n = len(arr)
    for i in arr:
        if i<0:
            minus += 1
        if i>0:
            plus +=1
        else:
            zero +=1

    rounded = round(minus/n, 5), "\n", round(plus/n, 5), "\n", round(zero/n, 5)

    return rounded


print(plusMinus(numList))

