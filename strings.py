# 10

def letter_check(word, letter):
    for i in word:
        if letter in word:
            return True
        else:
            return False


letter_check("strawberry", "o")

# 11

def contains(big_string, little_string):
  return little_string in big_string

# 12
def common_letters(string_one, string_two):
  common = []
  for letter in string_one: # loop through first string and check that letter on second string, if not in list then append
    if (letter in string_two) and not (letter in common): # I don't need to loop through second string
      common.append(letter) # no need to create a variable for this since we are referencing a list
  return common # I need to pay attention of the indentations

# def common_letters(string_one, string_two):
#   common = []
#   for letter1 in string_one:
#     for letter2 in string_two:
#       if letter1 == letter2:
#     return letter1

common_letters('manhattan', 'san francisco')


# 13

def username_generator(first_name, last_name):
#     if len(first_name) < 3: THIS IS NOT NECESSARY
#         return first_name
#     elif len(last_name) < 4:
#         return last_name
    username = first_name[:3] + last_name[:4]
    return username

user = username_generator("Zoe", "Lee")

def password_generator(username):
    password = ""
    for i in range(0, len(username)):
        password += username[i-1] # this will return the previous index of i first. so before Z as a loop comes e
    print(password)

password_generator("ZoeLee")
