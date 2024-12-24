import random
names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]


students_score = {name: random.randint(1, 100) for name in names}
print(students_score)

passed_students = {name: marks for (
    name, marks) in students_score.items() if marks > 33}
print(passed_students)
