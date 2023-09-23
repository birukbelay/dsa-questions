def gradingStudents(grades):
    # Write your code here
    list_of_grades=[]
    for grade in grades:
        if grade <38:
            list_of_grades.append(grade)
        elif ((grade % 5) >2):
            list_of_grades.append(grade + 5-(grade%5))
        else:
            list_of_grades.append(grade)
    return list_of_grades

print(gradingStudents([48,53,54,56]))