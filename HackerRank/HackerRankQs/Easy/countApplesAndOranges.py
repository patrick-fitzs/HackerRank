def countApplesAndOranges(s, t, a, b, apples, oranges):

    orangeLanded = 0
    appleLanded = 0

    # count apples landing on sams house
    for i in apples:
        landingPosition = i + a
        if landingPosition >=s and landingPosition <= t:
            appleLanded += 1
            # this iterates 2+4, 4+4, -4+4 = 6,6,0 meaning 1 between s and t(7-10)

    # count the oranges landing on sams house
    for i in oranges:
        landingPosition1 = i + b
        if landingPosition1 >= s and landingPosition1 <=t:
            orangeLanded +=1
            # this iterates 3+12, -2+12, -4+12 = 15,10,8 meaning 2 between s and t(7-10)

    print(appleLanded)
    print(orangeLanded)

countApplesAndOranges(7, 10, 4, 12, [2,3,-4], [3,-2,-4])


