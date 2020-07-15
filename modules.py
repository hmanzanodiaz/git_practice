# Import random below:
import random

# Create random_list below:
random_list = []

# Create randomer_number below:

random_list = [random.randint(0,101) for x in range(0, 101)]

# Print randomer_number below:
randomer_number = random.choice(random_list)

print(randomer_number)


#2 this creates a plot using randon and matplotlib

#import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)
plt.show()

# 3 decimal using Decimal module


# Import Decimal below:

from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal(0.2 + 0.69)
two_decimal_round = round(two_decimal_points, 2)
print(two_decimal_round)

four_decimal_points = Decimal(0.53 * 0.65)
four_decimal_round = round(four_decimal_points, 4)
print(four_decimal_round)

# OR this is another way of doing it

# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# 4 importing functions from different py files using from/omport

# Import library below in script.py
from library import always_three

#library is the library.py and always_three is the function on it

# Call your function below:
always_three()

# In this lesson, we covered some of the Python Standard Library, but you can explore all the modules that come packaged with every installation of Python at the Python Standard Library documentation.

# This is just the beginning. Using a package manager (like conda or pip3), you can install any modules available on the Python Package Index.