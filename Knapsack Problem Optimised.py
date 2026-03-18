def knapsackProblem(capacity, weights, values):
    n = len(weights)
    dp = [0] * (capacity + 1) # use single row and not a full table

    for i in range(n):
        # we iterate backwards to prevent using items in the same pass
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
print(knapsackProblem(8, weights, values))

"""
An example of the first iteration below, with item weight = 2 and value = 3

dp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
w=8: max(dp[8]=0,  3 + dp[8-2]) = max(0, 3 + dp[6]=0) → 3
w=7: max(dp[7]=0,  3 + dp[7-2]) = max(0, 3 + dp[5]=0) → 3
w=6: max(dp[6]=0,  3 + dp[6-2]) = max(0, 3 + dp[4]=0) → 3
w=5: max(dp[5]=0,  3 + dp[5-2]) = max(0, 3 + dp[3]=0) → 3
w=4: max(dp[4]=0,  3 + dp[4-2]) = max(0, 3 + dp[2]=0) → 3
w=3: max(dp[3]=0,  3 + dp[3-2]) = max(0, 3 + dp[1]=0) → 3
w=2: max(dp[2]=0,  3 + dp[2-2]) = max(0, 3 + dp[0]=0) → 3

"""