"""
Searching Challenge

Have the function SearchingChallenge(strArr) read in the strArr parameter
containing key:value pairs where the key is a string and the value is an integer.
Your program should return a string with new key:value pairs separated by a comma
such that each key appears only once with the total values summed up.

Your final output string should return the keys in alphabetical order.
Exclude keys that have a value of 0 after being summed up.

Examples:
Input:  ["B:-1", "A:1", "B:3", "A:5"]
Output: A:6,B:2

Input:  ["X:-1", "Y:1", "X:-4", "B:3", "X:5"]
Output: B:3,Y:1

Input:  ["Z:0", "A:-1"]
Output: A:-1
"""

def SearchingChallenge(strArr):
    counts = {}

    for item in strArr:
        key, val = item.split(":")
        counts[key] = counts.get(key, 0) + int(val)

    # remove keys that sum to 0
    counts = {k: v for k, v in counts.items() if v != 0}

    # sort alphabetically and build output string
    result = ",".join(f"{k}:{counts[k]}" for k in sorted(counts))

    return result


# Tests
print(SearchingChallenge(["B:-1", "A:1", "B:3", "A:5"]))   # A:6,B:2
print(SearchingChallenge(["X:-1", "Y:1", "X:-4", "B:3", "X:5"]))  # B:3,Y:1
print(SearchingChallenge(["Z:0", "A:-1"]))   # A:-1


def searchingChallenge(strArr):
    counts = {}

    for item in strArr:
        key, val = item.split(":")
        counts[key] = counts.get(key, 0) + int(val)

    counts = {k: v for k, v in counts.items() if v!= 0}

    result = ",".join(f"{k}:{counts[k]}" for k in sorted(counts))

    return result