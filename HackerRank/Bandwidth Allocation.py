"""
You are given n API endpoints numbered from 1 to n, and a total of m bandwidth units to distribute among them.

Allocate the bandwidth such that:
- All m units are fully allocated
- Each endpoint receives at least 1 unit
- The absolute difference in bandwidth between any two adjacent endpoints is at most 1

Determine the maximum possible bandwidth that can be assigned to the k-th endpoint while satisfying these conditions.

Function:
findMaximumBandwidths(n, k, m) -> int
Constraints:
1 <= n <= 1e9
1 <= k <= n
n <= m <= 1e9
"""

def findMaximumBandwidths(n, k, m):
    """
    Binary search the value x = bandwidth at position k.

    For a given x, the cheapest (minimum-sum) valid array that has a[k]=x
    is a "pyramid" that decreases by 1 per step away from k, but never below 1.
    If that minimum required sum <= m, then x is feasible.
    """

    def required_sum(x):
        left = k - 1        # number of endpoints left of k
        right = n - k       # number of endpoints right of k

        # ---- sum on the left side (excluding the center x) ----
        if x > left:
            # We can decrease by 1 all the way to the left edge without hitting 1.
            # Values: x-1, x-2, ..., x-left
            left_sum = (x - 1 + (x - left)) * left // 2
        else:
            # We hit 1 before the left edge.
            # Values: x-1, x-2, ..., 1 then remaining are 1s.
            left_sum = (x - 1) * x // 2
            left_sum += left - (x - 1)

        # ---- sum on the right side (excluding the center x) ----
        if x > right:
            # Values: x-1, x-2, ..., x-right
            right_sum = (x - 1 + (x - right)) * right // 2
        else:
            # Values: x-1, x-2, ..., 1 then remaining are 1s
            right_sum = (x - 1) * x // 2
            right_sum += right - (x - 1)

        return left_sum + x + right_sum

    low, high = 1, m
    ans = 1

    while low <= high:
        mid = (low + high) // 2

        if required_sum(mid) <= m:
            ans = mid       # mid is feasible, try higher
            low = mid + 1
        else:
            high = mid - 1  # mid too big, try lower

    return ans


print(findMaximumBandwidths(6, 2, 11))


#binary search scaling down like a pyramid
