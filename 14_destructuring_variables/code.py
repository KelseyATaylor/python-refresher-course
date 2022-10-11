# x = (5, 11)
# You don't need the parenthesis for python to recognize the tuple

t = 5, 11
x, y = t

print(x, y) #prints 5 11
# ^^This is what destructuring really means

# -- Destructuring in for loops --

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


# -- Another example --

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# The below technically still works but it's much less readable than destructuring at the for loop level

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


# -- Ignoring values with underscore --

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic

# -- Collecting values --
# * is the syntax for collecting. So all of destructured valued are being stored in the variable "tail"

head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]


*head, tail = [1, 2, 3, 4, 5]

print(head)  # [1, 2, 3, 4]
print(tail)  # 5