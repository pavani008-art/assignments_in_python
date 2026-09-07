# Create a list of student performance
students = ["Pavani", "Anu", "varshini", "Sita", "veda"]
print("Original list:", students)
# Display the list
print(students)
# Add an element
students.append("Anu")
print("After append:", students)
# Insert an element
students.insert(1, "Priya")
print("After insert:", students)
# Remove an element
students.remove("Sita")
print("After remove:", students)
# Sort the list
students.sort()
print("After sort:", students)
# Reverse the list
students.reverse()
print("After reverse:", students)
# Find length
print("Length:", len(students))

# Create a tuple containing 5 objects
student_tuple = ("Mani", "Gita", "Ravi", "Sita", "Kiran")
print("Tuple:", student_tuple)
# Access first element
print("First element:", student_tuple[0])
# Access last element
print("Last element:", student_tuple[-1])
# Find length of tuple
print("Tuple length:", len(student_tuple))