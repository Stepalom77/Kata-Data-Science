students = ["Daniel", "David", "Damian", "Denis"]

best_students = []

for s in students:
    if "David" not in s:
     best_students.append(s)

print(best_students)

[print(student) for student in students if "David" not in student]
