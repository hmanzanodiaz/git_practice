# 1
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

# my solution --> wrong

# while len(students_in_poetry) < 6:
#     students_in_poetry.insert(0, all_students.pop(0))
#     print(students_in_poetry)


while len(students_in_poetry) < 7:
    student = all_students.pop() # takes one out
    students_in_poetry.append(student) # adds it to empty list

print(students_in_poetry)
print(all_students)

# 2

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location) # prints the 3 elements of sales_data
  for element in location:
    scoops_sold += element # sums the location elements because its added to variable 0
print(scoops_sold)


# 3

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = []

for cel in celsius:
  conversion = cel * 9/5 +32
  fahrenheit.append(conversion)
print(fahrenheit)

# 4

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = []
cubes = []

for digit in single_digits:
  print(digit)
  square = digit ** 2
  squares.append(square)
  cube = digit ** 3
  cubes.append(cube)
print(squares)
print(cubes)

# 5

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for i in prices:
  total_price += i # add up all the prices to 255
print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices] # list comprehensive --> where EXPRESSION of MEMBER in LIST
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  print(i)

week_total = 0
for w in last_week:
  week_total += w
print(week_total)

total_revenue = total_price * week_total
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)