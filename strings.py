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
#     if len(first_name) < 3:
#     username = first_name
#     else:
#
#     return username
#     if len(last_name) < 4:
#     username = last_name
    username = first_name[:3] + last_name[:4]
    return username

user = username_generator("Zo", "Lee")
print(user)

def password_generator(username):
    password = ""
    for i in range(0, len(username)):
        password += username[i-1] # this will return the previous index of i first. so before Z as a loop comes e
    print(password)

password_generator("ZoeLee")

# 14

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(", ")
print(author_names)

author_last_name = []
for names in author_names:
  author_last_name.append(names.split()[-1]) # what I do is to take each index (names) and split it. then take the last index from that sublist

print(author_last_name)

# 15

# def evens(name):
#     for i in len(name):
#         if i % 2 == 0:
#             return name[i]
# evens("Watermelon")

def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")

# 15

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for words in love_maybe_lines:
  love_maybe_lines_stripped.append(words.strip()) # Appending on one list the strips os words

love_maybe_full = "\n".join(love_maybe_lines_stripped) # joining in separate lines
print(love_maybe_full)

#16
def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)

poem_title_card("Walt Whitman", "I Hear America Singing")

#17

