# # Creating a dictionary using curly braces
# student = {
#     "name": "Alice",
#     "age": 20,
#     "major": "Computer Science"
# }

# # Creating a dictionary using the dict() constructor with keyword arguments
# student_2 = dict(name="Bob", age=22, major="Engineering")

# # Creating a dictionary using the dict() constructor with a list of tuples
# student_3 = dict([("name", "Charlie"), ("age", 19), ("major", "Mathematics")])

# print(student)
# print(student_2)
# print(student_3)

# student = {
#     "name": "Alice",
#     "age": 20,
#     "major": "Computer Science"
# }
# print(student.items())
# # Adding a new key-value pair
# student["city"] = "New York"
# print(student) # Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'city': 'New York'}

# # Modifying an existing value
# student["age"] = 21
# print(student) # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'city': 'New York'}

# # Removing a key-value pair using del
# del student["city"]
# print(student) # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science'}

# # Removing a key-value pair using pop()
# major = student.pop("major")
# print(student) # Output: {'name': 'Alice', 'age': 21}
# print(major)   # Output: Computer Science

# student = {
#     "name": "Alice",
#     "age": 20,
#     "major": "Computer Science"
# }

# Getting keys
# keys = student.keys()
# print(keys) # Output: dict_keys(['name', 'age', 'major'])

# # Getting values
# values = student.values()
# print(values) # Output: dict_values(['Alice', 20, 'Computer Science'])

# # Getting items
# items = student.items()
# print(items) # Output: dict_items([('name', 'Alice'), ('age', 20), ('major', 'Computer Science')])

# # Updating the dictionary
# student.update({"city": "New York", "gpa": 3.8})
# print(student) # Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'city': 'New York', 'gpa': 3.8}

# # Popping an item
# age = student.pop("age")
# print(student) # Output: {'name': 'Alice', 'major': 'Computer Science', 'city': 'New York', 'gpa': 3.8}
# print(age)     # Output: 20

# # Clearing the dictionary
# student.clear()
# print(student) # Output: {}

# config = {
#     "database_host": "localhost",
#     "database_port": 5432,
#     "debug_mode": True,
#     "log_level": "INFO"
# }

# print(f"Database Host: {config['database_host']}")
# print(f"Debug Mode: {config['debug_mode']}")


# phonebook = {
#     "Alice": "123-456-7890",
#     "Bob": "987-654-3210",
#     "Charlie": "555-123-4567"
# }

# print(f"Alice's phone number: {phonebook['Alice']}")

# # Adding a new contact
# phonebook["David"] = "111-222-3333"
# print(phonebook)

# # Removing a contact
# del phonebook["Bob"]
# print(phonebook)

# def word_frequency(text):
#     """
#     Calculates the frequency of each word in a string.

#     Args:
#         text: The input string.

#     Returns:
#         A dictionary where keys are words and values are their frequencies.
#     """
#     text = text.lower()
#     text = ''.join(c for c in text if c.isalnum() or c.isspace()) # Remove punctuation
#     words = text.split()
#     frequency = {}
#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency

# text = "This is hard. This code is hard"
# print(word_frequency(text))
# #{'this': 2, 'is': 2, 'hard': 2, 'code': 1}


# def inverter(dictionary):
#     inverted_dictionary = {value : key for key, value in dictionary.items()}
#     return inverted_dictionary

# original_dictionary = {"A":1, "B": 2, "C": 3}
# print(inverter(original_dictionary))


def get_job_title(company_structure, employee_id):
    """
    Retrieves the job title of an employee from a nested dictionary.

    Args:
        company_structure: A nested dictionary representing the company's organizational structure.
        employee_id: The ID of the employee.

    Returns:
        The job title of the employee, or None if the employee is not found.
    """
    for keys, values in company_structure.items():
        if employee_id in values:
            return values[employee_id]
    return None

company_structure = {
    "Engineering": {
        101: "Software Engineer",
        102: "Data Scientist"
    },
    "Marketing": {
        201: "Marketing Manager",
        202: "Social Media Specialist"
    }
}

print(get_job_title(company_structure, 101))  # Output: Software Engineer
print(get_job_title(company_structure, 202))  # Output: Social Media Specialist
print(get_job_title(company_structure, 301))  # Output: None