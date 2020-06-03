# 1

#Write your function here
# check len of both list and return the largest. if equal return [-1] of lst1

def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst1) < len(lst2):
    return lst2[-1]
  else:
    return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# 2

# Write your function here
# if statement, count(),
def more_than_n(lst, item, n):
    counts = lst.count(item)
    if counts > n:
        return True
    else:
        return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# 3

#Write your function here
def append_size(lst):
  nums = [len(lst)]
  new_list = lst + nums
  return new_list

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# 4

#Write your function here
def combine_sort(lst1, lst2):
  new_list =lst1 + lst2
  new_list.sort()
  return new_list
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# 5

def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(109))

# 6

# ---- my code below
# #Write your function here
# # I need to remove the slice [start:end] = [1:3]
# def remove_middle(lst, start, end):
#   del lst[start:end + 1]
#   print(lst)
#
# #Uncomment the line below when your function is done
# print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


#---- correct code below
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 7

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) < lst.count(item2):
    return item2
  else:
    return item1

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# 8
#Write your function here
# I need to double index 2 and return new list
#  my option below
# def double_index(lst, index):
#     new_list = []
#     if True:
#       lst[index] = lst[in]*2
#       return new_list + lst
#     else:
#       return lst

#Uncomment the line below when your function is done
# print(double_index([3, 8, -10, 12], 2))

# codeacademy option below
#Write your function here
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# 9
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1] # with this I select the element that later I use to get the Index "int(len(lst)/2"
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

# 10
# Write your function here --> this will return the elements divisible by 10

def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i % 10 == 0:
      count += 1
  return count


# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 5
#Write your function here --> this will print each names on the list on a new list will Hello string
# need to print greeting with name on it. looping through the list and appending each element to new list string
def add_greetings(names):
  empty_list = []
  for name in names:
    empty_list.append("Hello, " + name)
  return empty_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))