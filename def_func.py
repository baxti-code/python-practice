# def greet(name):
#   """This function greets the person passed in as a parameter."""
#   print(f"Hello, {name}!")

# # Calling the function with an argument
# greet("Alice")  # Output: Hello, Alice!
# greet("Bob")    # Output: Hello, Bob!

# def describe_person(name, age, city):
#   """This function describes a person based on their name, age, and city."""
#   print(f"{name} is {age} years old and lives in {city}.")

# # Calling the function with multiple arguments
# describe_person("Charlie", 30, "New York") # Output: Charlie is 30 years old and lives in New York.
# describe_person("Diana", 25, "London")   # Output: Diana is 25 years old and lives in London.

# def power(base, exponent=2):
#   """This function calculates the power of a number.
#   If no exponent is provided, it defaults to 2 (square)."""
#   result = base ** exponent
#   return result

# # Calling the function with one argument (using the default exponent)
# square = power(5)  # base=5, exponent=2 (default)
# print(square)       # Output: 25

# # Calling the function with two arguments (overriding the default exponent)
# cube = power(5, 3)  # base=5, exponent=3
# print(cube)         # Output: 125

# def describe_pet(animal_type, pet_name):
#   """Display information about a pet."""
#   print(f"\nI have a {animal_type}.")
#   print(f"My {animal_type}'s name is {pet_name}.")

# describe_pet(animal_type='hamster', pet_name='Harry')
# describe_pet(pet_name='Lucy', animal_type='dog')

# def format_name(first_name, last_name, middle_name=''):
#     """Format a name."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# print(format_name("john", "doe"))
# print(format_name("john", "doe", middle_name="david"))
# print(format_name("john", last_name="doe", middle_name="david")) # Correct
# # print(format_name("john", middle_name="david", "doe")) # Incorrect - positional argument after keyword argument

# def add(x, y):
#   """This function adds two numbers and returns the result."""
#   sum_result = x + y
#   return sum_result

# # Calling the function and storing the returned value
# result = add(3, 5)
# print(result)  # Output: 8

# def calculate_stats(numbers):
#   """This function calculates the sum and average of a list of numbers."""
#   total = sum(numbers)
#   average = total / len(numbers)
#   return total, average

# # Calling the function and unpacking the returned tuple
# numbers = [1, 2, 3, 4, 5]
# sum_result, average_result = calculate_stats(numbers)
# print(f"Sum: {sum_result}, Average: {average_result}")  # Output: Sum: 15, Average: 3.0

# def print_message(message):
#   """This function prints a message to the console."""
#   print(message)
#   # No return statement here

# # Calling the function and checking the returned value
# result = print_message("Hello, world!")
# print(result)  # Output: None

# def convert_celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit


# result = convert_celsius_to_fahrenheit(30)
# print(result)

# def calculate_rectangle_area(length = 2, width = 1):
#     return length * width

# def reverse_string(text):
#     return text[::-1]

# x = reverse_string("String")
# print(x)

def calculate_tip(bill, tip_percentage = 15):
    return bill * (tip_percentage/100)

x = calculate_tip(100, 20)
print(x)