# 1
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

# my solution --> wrong

# while len(students_in_poetry) < 6:
#     students_in_poetry.insert(0, all_students.pop(0))
#     print(students_in_poetry)


while len(students_in_poetry) < 6:
    student = all_students.pop() # takes one
    students_in_poetry.append(student) # adds it to empty list

print(students_in_poetry)

# 2

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location) # prints the 3 elements of sales_data
  for element in location:
    scoops_sold += element # sums the location elements
print(scoops_sold)


# 3