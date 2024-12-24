import pandas
student_dict = {
    "student": ["Mayank", "Krishna", "Kunal"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through column of a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row.student)
    if (row.student == "Mayank"):
        print(row.score)
