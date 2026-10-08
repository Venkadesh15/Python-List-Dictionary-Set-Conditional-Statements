# LIST, DICTIONARY, SET & CONDITIONAL STATEMENTS

# -----------------LIST--------------------#

# 1. creating List of Name and Age 
age_list = [24, 25, 26, 27, 28]
name_list = ["Arun", "Bala", "Charan", "Divya", "Ezhil"]

# 2. operations on the list
# adding a new name and age to the list
name_list.append("Yazhini")
print(name_list)
age_list.insert(2, 30)
print(age_list)
# removing a name and age from the list
name_list.remove("Yazhini")
print(name_list)
age_list.pop()
print(age_list)
# extending the age again with ages
age_list.extend([29, 30, 26])
print(age_list)
# sorting the age list in descending order
age_list.sort(reverse=True)
print(age_list)
# finding the maximum, minimum and sum of ages
print("Age list:", age_list)
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))

# 3. accessing the name and age  
# accessing the first name using positive indexing
print("First name:", name_list[0])
# accessing the last name using negative indexing
print("Last name:", name_list[-1])
# accessing the names from index 2 to 4 using slicing
print("Names at indexes 2 to 4:", name_list[2:5])
# reversing the name list 
print("Names in reverse:", name_list[::-1])

#-----------------DICTIONARY--------------------#

# 1. create a dictionary of student details
student_marks = {
    "Arun": 76,
    "Bala": 91,
    "Charan": 68,
    "Divya": 84,
    "Ezhil": 73
}

# 2. accessing Bala's mark from the dictionary
print("Bala's mark:", student_marks["Bala"])

# 3. adding new student name and marks to the dictionary
student_marks["Janani"] = 80
student_marks["Charan"] = 82

# 4. student names, marks and student-mark pairs
print("Student names:", student_marks.keys())
print("Marks:", student_marks.values())
print("Student-mark pairs:", student_marks.items())

#-----------------SET--------------------#

# 1. creating a set of vowels
my_set = set(["a", "e", "i", "o", "u", "a", "a", "i"])
print("my_set:", my_set)

# 2. adding a new vowel to the set
try:
    my_set[4] = "s"
except TypeError:
    print("A set cannot be changed using an index.")
    print("Sets are unordered and do not support item assignment.")
    
# 3. performing union and intersection of two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}
# union of set1 and set2
print("Union:", set1 | set2)
# intersection of set1 and set2
print("Intersection:", set1 & set2)

#-----------------CONDITIONAL STATEMENTS--------------------#

# 1. if , elif and else statements
score = int(input("Enter your score (0 to 10): "))
# checking the score and printing the corresponding message
if score < 0 or score > 10:    
    print("Please enter a score from 0 to 10.")
# greater than 7 is above average
elif score > 7:
    print("Above Average: Excellent work! Keep it up.")
# between 4 and 7 is average
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
# otherwise below average
else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")