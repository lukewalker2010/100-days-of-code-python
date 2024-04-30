# List and Dictionary Comprehensions

# List Comprehension (Unique to Python)
# Create new list using a previous list

# new_list = [new_item for item in list if test]

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

# range(1,5) [2, 4, 6, 8]

# new_range = [2*n for n in range(1,5)]
# print(new_range)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list(itterable)}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)
