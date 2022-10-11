friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

# print(friend_ages["Adam"])

# to change or update a key value pair (Or add one)

friend_ages["Bob"] = 20

print(friend_ages)
# Prints {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}

# -- List of dictionaries --
# Lists don't care about white space
# This is a list of dictionaries, and each dictionary represents a friend

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(friends)
print(friends[1])
print(friends[1]["name"])


# -- Iteration --

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}")

    # Better

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# -- Using the `in` keyword --

if "Bob" in student_attendance:
    print(f"Bob: {student_attendance[student]}")
else:
    print("Bob isn't a student in this class!")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))