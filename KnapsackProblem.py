"""

Let's say you have a bag that can hold 10kg.

There are items with weights and values

What items can you fit in your bag to get the maximum value while staying under the weight limit?

When traversing items we have 2 options, take or leave.
# Example
capacity = 8kg
weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]

"""

def knapsackProblem(capacity, weights, values):
    # n is the total amount of items
    n = len(weights)
    # our table to check all items.
    # Imagine a matrix, columns being weights and rows being items (have values)
    dp = [[0] * (capacity + 1) for _ in range(n+1)] # so [0] * 8+1 columns and 4+1 rows

    # now we traverse and see if the current item can fit
    for i in range(1, n+1):
        for w in range(1, capacity+1):

            # skip the item and add the value from above
            dp[i][w] = dp[i-1][w]

            #option 2, take if it fits / if current row in weights is less or equal to current position in table
            if weights[i-1] <= w:
                # take stores the value of current item(row) we're on + value at row above minus the weight
                take = values[i-1] + dp[i-1][w - weights[i-1]]
                # current position is max of calc above or current
                # (does taking beat skipping and populating current value with value above
                dp[i][w] = max(dp[i][w], take)
    # return the very past point in matrix i.e dp[n=4(last row)][capacity=8 (last column)]
    return dp[n][capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
print(knapsackProblem(capacity=8, weights=weights, values=values))