# ============ List ============

# 1. List Creation
age_list = [24, 25, 26, 27, 28]
name_list = ["Arun", "Divya", "Karthik", "Meena", "Suresh"]

# 2. List Operations / Modifications
name_list.append("Yazhini")
print("a.", name_list)

age_list.insert(2, 30)
print("b.", age_list)

name_list.remove("Yazhini")
print("c.", name_list)

age_list.pop()
print("d.", age_list)

age_list.extend([29, 30, 26])
print("e.", age_list)

age_list.sort(reverse=True)
print("f.", age_list)

print("g. Max age:", max(age_list))
print("g. Min age:", min(age_list))
print("g. Sum of ages:", sum(age_list))

# 3. Accessing List Elements
print("a.", name_list[0])
print("b.", name_list[-1])
print("c.", name_list[2:5])
print("d.", name_list[::-1])

# ============ Dictionary ============

# a. Create dictionary
student_marks = {"Arun": 78, "Divya": 91, "Karthik": 65, "Meena": 88, "Suresh": 72}

# b. Access a specific student's mark
print("b.", student_marks["Divya"])

# c. Add new student
student_marks["Janani"] = 80
print("c.", student_marks)

# d. Update an older student's mark
student_marks["Arun"] = 82
print("d.", student_marks)

# e. keys(), values(), items()
print("e. Keys:", student_marks.keys())
print("e. Values:", student_marks.values())
print("e. Items:", student_marks.items())

# ============ Sets (Operations) ============

# a. Create a set from the list of values
my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print("a.", my_set)
# Explanation: A set stores only unique elements, so the duplicate 'a' and 'i'
# are removed. The output has just 5 vowels: a, e, i, o, u. The order may
# change on each run because sets are unordered.

# b. Attempt to change an element by index
try:
    my_set[4] = 's'
except TypeError as e:
    print("b. Error:", e)
# Explanation: Sets are unordered, so elements have no index positions.
# Item assignment is not supported, which raises:
# TypeError: 'set' object does not support item assignment

# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Union and intersection
print("d. Union:", set1 | set2)
print("d. Intersection:", set1 & set2)
# Explanation.The error is because the set had repetation.set should be unique.
# ============ Performance Category Program ============

score = float(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a value between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! Keep up the great performance.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")