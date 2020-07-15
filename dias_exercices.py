from datetime import datetime

birthday = datetime(1986, 5, 7, 16, 14)
print(birthday.weekday())

print(datetime.now())

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

# strptime allow us to take a string, parse through it and return a datetime

parsed_date = datetime.strptime("Jan 14 2018", "%b %d %Y") # formated string
print(parsed_date)
print(parsed_date.month)

# strftime allow us to take a datetime and get a string datetime

string_time = datetime.strftime(datetime.now(), "%b %d %Y")
print(string_time)