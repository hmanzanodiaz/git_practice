# A class = is a template for a data type. It describes the kinds of information that class will hold and how a programmer
# will interact with that data. Define a class using the class keyword
# A class doesn’t accomplish anything simply by being defined. A class must be instantiated. In other words, we must create an instance of the class (OBJECT), in order to breathe life into the schematic.
# Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined CoolClass as follows:
# cool_instance = CoolClass()
# Above, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable cool_instance for safe-keeping so we can access our instance of CoolClass at a later time.
# A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.
# You can define a class variable by including it in the indented part of your class definition, and you can access all of an object’s class variables with object.variable syntax.
# we create objects when we instantiate a class, we find the class when we check the type() of an object
# We learned the difference between class variables (the same for all objects of a class) and instance variables (unique for each object).
# We learned about how to define an object’s functionality with methods. We created multiple objects from the same class, all with similar functionality, but with different internal data. They all had the same methods, but produced different output because they were different instances.


# 1 Create a Grade class with a class attribute minimum_passing equal to 65.
class Grade:
  minimum_passing = 65

# Below we defined the class Musician, then instantiated drummer to be an object of type Musician. We then printed out the drummer’s .title attribute, which is a class variable that we defined as the string “Rockstar”.

class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"

# 2
# METHOD = Methods are functions that are defined as part of a class. The first argument in a method is always the object that is calling the method. Convention recommends that we name this first argument self. Methods always have at least this one argument.

class Circle:
  pi = 3.14

  def area(self, radius):
    # Give Circle an area method that takes two parameters: self and radius.
    return Circle.pi * radius ** 2
  # Since pi is a class variable, you can access it as an attribute of the class.

circle = Circle() # this is an instance
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

# 3
# CONSTRUCTOR: The first dunder method we’re going to use is the __init__ method (note the two underscores before and after the word “init”).
# This method is used to initialize a newly created object. It is called every time the class is instantiated.
# Methods that are used to prepare an object being instantiated are called constructors.

class Circle:
  pi = 3.14 # this is a class variable

  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: " + str(diameter))


teaching_table = Circle(36)


# 4 INSTANCE VARIABLE
# We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class,
# but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has?
# This is because each instance of a class can hold different kinds of data.
# The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances
# of a class — they are variables that are specific to the object they are attached to.
# We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables to
# these objects using the same attribute notation that was used for accessing class variables.

class Store:
  pass

alternative_rocks = Store() # instantiate object
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks" # instance variable
isabelles_ices.store_name = "Isabelle's Ices"

# 5 ATTRIBUTE FUNCTIONS
# Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both
# considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an
# instance variable of the object Python will throw an AttributeError.

# hasattr(attributeless, "fake_attribute")
# returns False

# getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

# -----

how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"): # count is the argument
    print(element.count("s")) #element.count is the instance variable

# instance variable is data unique to that instance

class Circle:
  pi = 3.14 # class variable

  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:

    self.radius = diameter / 2 # instance variable. radius is an attribute

  def circumference(self): #method
    return 2 * self.pi * self.radius


medium_pizza = Circle(12) # Class instance or object. 12 is an argument of that object
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# __repr__ We learned about the dunder method __init__. Now, we will learn another dunder method called __repr__.
# This is a method we can use to tell Python what we want the string representation of the class to be. __repr__ can
# only have one parameter, self, and must return a string.

class Circle:
  pi = 3.14

  def __init__(self, diameter):
    self.radius = diameter / 2

  def area(self):
    return self.pi * self.radius ** 2

  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# CLASS project

class Student():
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade.score)

class Grade():
  minimum_passing = 65
  def __init__(self, score):
    self.score = score


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
