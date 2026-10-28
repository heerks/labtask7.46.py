"""Program:01"""

# Create a set containing five different fruits and print it.

fruits = {"apple", "mango", "banana", "orange", "grapes"}
print(" {fruits}")



"""Program:02"""

# Given numbers = [2, 4, 2, 6, 4, 8, 8], convert the list into a set to remove duplicates.
numbers = [2, 4, 2, 6, 4, 8, 8]
numbers_set = set(numbers)
print(" {numbers_set}")



"""Program:03"""

# Create a set of five numbers. Add 10 to the set and remove one existing number.
my_set = {1, 2, 3, 4, 5}
my_set.add(10)
my_set.remove(3) # removing 3
print(" {my_set}")

"""Program:04"""

# Ask the user for a number and check whether it exists in the set {10, 20, 30, 40, 50}.
check_set = {10, 20, 30, 40, 50}
user_num = int(input(" Enter a number to check: "))
if user_num in check_set:
    print("{user_num} exists in the set")
else:
    print("{user_num} does not exist in the set")

"""Program:05"""

# Given values = {1, 2, 2, 3, 3, 3, 4}, predict the length of the set and explain why.
values = {1, 2, 2, 3, 3, 3, 4}
print(" Length is {len(values)}")
# Explanation: Set automatically removes duplicate values, so {1,2,2,3,3,3,4} becomes {1,2,3,4} with length 4.

"""Program:06"""

# Practice the four important operations: union (|), intersection (&), difference (-), and symmetric difference (^).
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Find all unique elements in A and B.
# Using the same sets, find elements common to both sets.
# Find A - B and B - A. Explain why their results differ.
# Find elements that are in either A or B, but not in both.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# All unique elements in A and B (Union)
print(" Union (A | B): {A | B}")

# Elements common to both sets (Intersection)
print(" Intersection (A & B): {A & B}")

# A - B and B - A (Difference)
print(" A - B: {A - B}")
print(" B - A: {B - A}")
# Explanation: A-B gives elements only in A, B-A gives elements only in B, so results differ because difference is not commutative.

# Elements that are in either A or B, but not in both (Symmetric Difference)
print(" Symmetric Difference (A ^ B): {A ^ B}")