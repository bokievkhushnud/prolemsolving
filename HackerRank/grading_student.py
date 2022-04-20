import math
grades = [73, 67, 38, 33]
def gradingStudents(grades):
    new_grades=[]
    for i in grades:
        next_multiple=math.ceil(i/5)*5
        if i>=38:
            if next_multiple-i<3:
                new_grades.append(next_multiple)
            elif next_multiple-i>=3:
                new_grades.append(i)
        else:
            new_grades.append(i)
    return new_grades
print(gradingStudents(grades))