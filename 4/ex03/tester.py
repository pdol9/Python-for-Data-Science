from new_student import Student


student = Student(name = "Edward", surname = "agle")
print(student)

# this returns error as login and id should not be initializable
student = Student(name = "Edward", surname = "agle", id = "toto")
print(student)
