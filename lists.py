#These codes below are practices i did when i was learning 

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[0][1])  

# my_list = ["apple", "banana", "cherry"]
# my_list.pop()
# print(my_list)

# my_colors = ["red", "green", "blue", "yellow"]

# print(my_colors[1])
# print(my_colors[-1])

# primary_colors = my_colors[:3]
# print(primary_colors)

# my_colors[3] = "orange"
# print(my_colors)

# my_colors.append("purple")
# print(my_colors)

# my_colors.insert(1, "teal")
# print(my_colors)

# my_colors.remove("green")
# print(my_colors)

# my_colors.pop(3)
# print(my_colors)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# greater_numbers = [x for x in numbers if x > 5]
# print(greater_numbers)

# my_list = [1, 2, 3]
# my_list.insert(10, 4)
# print(my_list) # Output: [1, 2, 3, 4]
# # Example: Extending a list with another list
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# # Extending with a tuple
# my_list = ["apple", "banana"]
# my_list.extend(("cherry", "date"))
# print(my_list) # Output: ['apple', 'banana', 'cherry', 'date']

# # Extending with a string (adds each character as an element)
# my_list = [1, 2, 3]
# my_list.extend("456")
# print(my_list) # Output: [1, 2, 3, '4', '5', '6']

# # Example: Concatenating lists using the + operator
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# new_list = list1 + list2
# print(new_list)  # Output: [1, 2, 3, 4, 5, 6]
# print(list1) # Output: [1, 2, 3] (list1 is unchanged)
# print(list2)

# # Combining different data types (requires type consistency)

# list1 = [1, 2, "hello"]
# list2 = [3.14, True]
# new_list = list1 + list2
# print(new_list) # Output: [1, 2, 'hello', 3.14, True]

#Example: Removing an element by value

# my_list = [1, 2, 3, 2]
# my_list.remove(2)  # Removes the first occurrence of 2
# print(my_list)  # Output: [1, 3, 2]

# # # Removing a string

# my_list = ["apple", "banana", "cherry", "banana"]
# my_list.remove("banana")
# print(my_list) # Output: ['apple', 'cherry', 'banana']

# Handling ValueError if the element is not found
# my_list = [1, 2, 3]
# try:
#     my_list.remove(4)
# except ValueError:
#     print("Element not found in the list") # Output: Element not found in the list

# Example: Removing an element by index
# my_list = [1, 2, 3]
# removed_element = my_list.pop(1)  # Removes the element at index 1 (which is 2)
# print(my_list)  # Output: [1, 3]
# print(removed_element)  # Output: 2

# # Removing the last element
# my_list = ["apple", "banana", "cherry"]
# removed_element = my_list.pop()
# print(my_list) # Output: ['apple', 'banana']
# print(removed_element) # Output: cherry
# # Handling IndexError if the index is out of range
# my_list = [1, 2, 3]
# try:
#     removed_element = my_list.pop(5)
# except IndexError:
#     print("Index out of range") # Output: Index out of range

# Example: Sorting a list in ascending order
# my_list = [3, 1, 4, 1, 5, 9, 2, 6]
# my_list.sort()
# print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# # Sorting a list of strings alphabetically
# my_list = ["banana", "apple", "cherry"]
# my_list.sort()
# print(my_list) # Output: ['apple', 'banana', 'cherry']

# # Sorting in descending order
# my_list = [3, 1, 4, 1, 5, 9, 2, 6]
# my_list.sort(reverse=True)
# print(my_list)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# # Sorting with a custom key function
# my_list = ["banana", "Apple", "cherry"]
# my_list.sort(key=str.lower) # Sorts case-insensitively
# # print(my_list) # Output: ['Apple', 'banana', 'cherry']

# # Example: Sorting a list of tuples based on the second element
# my_list = [(1, 'z'), (2, 'a'), (3, 'b')]
# my_list.sort(key=lambda item: item[1])  # Sort by the second element of each tuple
# print(my_list)  # Output: [(2, 'a'), (3, 'b'), (1, 'z')]

# # Sorting a list of dictionaries based on a specific key
# my_list = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
# new_list = sorted(my_list, key=lambda item: item['age']) # Sort by the 'age' key
# print(new_list) # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]


# grocery_list = ["milk", "eggs", "bread"]
# grocery_list.insert(0, "cheese")
# grocery_list.append("spinach")
# grocery_list.remove("eggs")
# grocery_list.sort()
# print(grocery_list)


# numbers = [3, 8, 12, 24, 1, 2, 5]
# new_numbers = sorted(numbers, reverse=True)
# print(numbers)
# print(new_numbers)

# students = [("Baxti", 99), ("Berdi", 95), ("Diyor", 80), ("Aziz", 85)]
# students.sort(key = lambda x : x[1])
# print(students)

def length(strings):
    return len(strings)

string_list = ["Hi", "Hello", "Bye", "GoodBye", "NiceToMeetYou", "Pleased", "Ok"] 

string_list.sort(key= length)
print(string_list)


#To be continued
#...