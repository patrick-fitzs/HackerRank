# Take an array of grades, the first int n is the number of students, this is taken off in the function on the HackerRankQs testcode
# to do it here, simple slice
grades = [4, 73, 67, 38, 33]

def gradingStudents(grades):
    roundedGrades = []
    for grade in grades:
        if grade < 38:
            roundedGrades.append(grade)
        else:
            nextMultipleOf5 = ((grade//5) +1) *5
            if nextMultipleOf5 - grade < 3:
                roundedGrades.append(nextMultipleOf5)
            else:
                roundedGrades.append(grade)
    return roundedGrades

print(gradingStudents(grades))