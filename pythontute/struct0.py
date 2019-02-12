
students = []

for i in range(3):
    name = input("Name: ")
    dorm = input("Dorm: ")

    student = {"name": name, "dorm": dorm}
    students.append(student)

for student in students:
   print(f"{student['name']} is in this{student['dorm']}")
