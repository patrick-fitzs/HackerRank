def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Calculate apples landing on the house
    appleLanded = sum(1 for i in apples if s <= i + a <= t)


    # Calculate oranges landing on the house
    orangeLanded = sum(1 for i in oranges if s <= i + b <= t)

    # Print the results on separate lines
    print(appleLanded)
    print(orangeLanded)

countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])

# test
x = 10
y = 11
