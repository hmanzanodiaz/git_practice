# 1

#Write your function here
# check len of both list and return the last item. if equal return [-1] of lst1

def larger_list(lst1, lst2):
  if len(lst1) > len(lst2): # len() returns the number of elements on a list. here only looks at the number of elements and not the value
    return lst1[-1] # here is returning the list if met the condition
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
    counts = lst.count(item) # counts how many times an element is on a list
    if counts > n:
        return True
    else:
        return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# 3

#Write your function here
def append_size(lst):
  nums = [len(lst)] # creates a new list with the length of LST
  new_list = lst + nums # this joins the elements of LST and adds the number of elements of LST in new_list
  return new_list # [23, 42, 108, 3]

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# 4

#Write your function here
def combine_sort(lst1, lst2):
  new_list = lst1 + lst2 # combines 2 lists
  new_list.sort() # sort() sorts that new_list in an ascending order. Sort() modifies same list, whether sorted() creates a new list
  return new_list
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# 5

def every_three_nums(start):
  return list(range(start, 101, 3)) # list() creates a list of the range (start, 101) returning every 3 numbers

#Uncomment the line below when your function is done
print(every_three_nums(80))

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
  return lst[:start+1] + lst[end+1:] # this take the first and last item +1 (to be inclusive), an returns those values
# slicing is use to return part of the indexes of a list

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 7

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2): # count(item) looks at how many times that item is on the list
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
# Write your function here to double index in the middle
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst): # checks whether index(2) is greater than 4
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index] # creates a new list from 3 to -10 (index 0:2 not including 2)
 # Adds double the value at index to the new list
  new_lst.append(lst[index]*2) # appends to the new list the calculation of index 2 (-10) * 2 and adds it.
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:] # here adds the rest of the indexes from original list
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# 9

def middle_element(lst):
  if len(lst) % 2 == 0: # checking whether the length of the list is divisible by 2 (6/2 == 0 --> YES)
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1] # first part takes -4 and second one -10 = -14
# first part take half of the list length () and returns the INT of that index. second part same but adding 1 more index, (-4)
    return sum / 2 # takes -14 divided by 2 == -7.0
  else:
    return lst[int(len(lst)/2)] # looks like int rounds up to take the 4th index -4

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

# 10
# Write your function here --> this will return the elements divisible by 10

def divisible_by_ten(nums):
  count = 0 # create empty variable that will store the final value
  for i in nums: # this goes through every index on the list
    if i % 10 == 0: # checks element i to see if is divisible by 10
      count += 1 # adds one more element to the variable with initial value 0, to return final count = 3. so COUNT will return only the aggregation
  return count
# this helps count the number of elements that meet my criteria

# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 5
#Write your function here --> this will print each names on the list on a new list will Hello string
# need to print greeting with name on it. looping through the list and appending each element to new list string
def add_greetings(names):
  empty_list = [] # creates a new empty list to store final result
  for name in names: #takes each name and append with a string into new list
    empty_list.append("Hello, " + name)
  return empty_list #returns new list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# 6
# #Write your function here ---> remove even numbers
#
# # for loop, divisible by 2, if statement, new empty list, return i that meet the condition
#
# def delete_starting_evens(lst):
#   new_list = 0
#   for i in lst:
#     if i % 2 != 0:
#       new_list += 1
#
#   return new_list
#
# #Uncomment the lines below when your function is done
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(delete_starting_evens([4, 8, 10]))

# code academy solution below

#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0): #checks for whether the list has more than 1 number and index (value) is divisible by 2
    lst = lst[1:] # Line 3 states that if it is an even number, lst should now equal lst with the first index (index 0) removed.
  return lst

# Use a while loop to check two things. First, check if the list has at least one element, using len(lst) . Second, check to see if the first element is odd using mod ( % ).
# If both of those are True, slice off the first element of the list using lst = lst[1:] .

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# --- another way of looking at it

def delete_starting_evens(lst):
  while lst and lst[0] % 2 == 0:
    lst.pop(0)
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


# 7
# Write your function here
def odd_indices(lst):
  odd_list = [lst[i] for i in range(len(lst)) if i % 2 == 1]
  return odd_list


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))


# 8
#Write your function here to Return a new list containing every number in bases raised to every number in powers.
def exponents(bases, powers):
  lst = [b**e for b in bases for e in powers] # 2 for loops to take b index and multiply by e index
  return lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

# 9
# Write your function here
# sum both lists and return the one that is larger

def larger_sum(lst1, lst2):
  blk1 = 0
  blk2 = 0
  for i in lst1:
    blk1 += i
  for i in lst2:
    blk2 += i
  if blk1 > blk2:
    return lst1
  elif blk1 < blk2:
    return lst2
  else:
    return lst1

# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# 10

#Write your function here
def over_nine_thousand(lst):
  nine = 0
  for i in lst:
    nine += i
  while nine < 9000:
    return lst
  else:
    return nine

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# 11

#Write your function here
def over_nine_thousand(lst):
  num = 0
  for i in lst:
    num += i # I got it right until here. it return the total sum of the list but not over  9000
    if (num > 9000): # the IF needed to be indented and added a BREAK to stop when arrive to 9000
      break
  return num


#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# 12

 #Write your function here
def max_num(nums):
  max = nums[0] # I initially created a variable 0. but I needed to look at index 0 value 50 to start comparing
  for i in nums:
    if i > max:
     max = i
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# 13

# equals = [a for a in lst1 for b in lst2 if a == b]
#  return equals

# def same_values(lst1, lst2):
#     equals = []
#     for a in lst1:
#       for b in lst2:
#         if a == b:
#           equals.append(a)
#     return equals

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)): # range() and len() looks at the index and not the value of it. range(len(obj)) to iterate over the numbers from 0 up to the length of the iterable obj.
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 14
# #Write your function here
# my solution not correct below ----------

# def reversed_list(lst1, lst2):
#   reverse = lst1.sort(reverse=True)
#   if lst2 == reverse:
#     return True
#   else:
#     return False

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)): # going through the range of indexes
    if lst1[index] != lst2[len(lst2) - 1 - index]: # starts at the end and move through indexes in reverse order
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))





