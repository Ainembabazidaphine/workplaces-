"""
Problem:a school wants to store a student's name,age,marks from three  tests
and a collection of related details
Decomposition:
student_name(string),student_age(int),all marks(float),
 comments(string),student_marks(list),student_details()

"""

student_name = "Daphine"
student_age = 20

student_marks = [85.5, 90.0, 81.0]

Student_details = {
    "Name": student_name,
    "Age": student_age,
    "Marks": student_marks
}

print( Student_details["Name"])
print( Student_details["Age"])
print(Student_details["Marks"])
print(student_marks[0])

print(type(student_name))
print(type(student_age))
print(type(student_marks))
print(type(Student_details))
