# # def temperature():
# #     celcius = input("Enter the celcius: ")
# #     celcius = float(celcius)
# #     fahrenheit = (celcius * (9/5))+32
# #     return fahrenheit
    
# # print(temperature())

# def len_rev(my_string):
#     return len(my_string), list(reversed(my_string))

# print(len_rev("Bakhti"))

# def seerange(my_list):
#     return max(my_list)-min(my_list)

# print(seerange([1, 2, 3, 4, 5,6]))

# my_list = ["I", "am", "Baxti"]

# result = ""

# for char in my_list:
#     result+=char

# result = str(result)

# print(result)

# import math

# def calculate_circle_area(radius):
#   """
#   Calculates the area of a circle.

#   Args:
#     radius: The radius of the circle.

#   Returns:
#     The area of the circle.
#   """
#   area = math.pi * (radius ** 2)
#   return area

# # Example usage
# circle_radius = 7
# circle_area = calculate_circle_area(circle_radius)
# print("The area of the circle is:", circle_area)  # Output: 153.93804002589985

global_variable = 10  # Global scope

# def my_function():
#     local_variable = 5  # Local scope
#     print("Inside the function:")
#     print("Global variable:", global_variable)
#     print("Local variable:", local_variable)

# my_function()

# print("Outside the function:")
# print("Global variable:", global_variable)
# # print("Local variable:", local_variable)  # This will cause an error, as local_variable is not accessible here

# def calculate_trapezoid_area(base1, base2, height):
#     """
#     Calculates the area of a trapezoid

#     Args:
#          base1 : the base of a trapezoid
#          base2 : the second base of a trapezoid
#          height : the height of a trapezoid

#     Returns:
#         The area of the trapezoid

#     """

#     area = (base1+base2)/2 * height
#     return area
# print(calculate_trapezoid_area(5, 13, 10))



# def calculate_square_area(side):
#     area = side * side
#     return area

# print(calculate_square_area(5))
# import math
# def calculate_combined_area(rectangle_length, rectangle_width, circle_radius):
#     rectangle_area = rectangle_length * rectangle_width
#     circle_area = math.pi * circle_radius ** 2
#     combined_area = rectangle_area + circle_area
#     return f"{combined_area:.2f}"

# print(calculate_combined_area(5, 10, 4))

# def calculate_rectangle_area(length, width):
#     if length <= 0:
#         print("Invalid input: Length and width must be positive.")
#     elif width <=0:
#         print("Invalid input: Length and width must be positive.")
#     else:
#         area = length * width
#         return area

# # Example usage
# rectangle_length = -1
# rectangle_width = -1
# rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
# print("The area of the rectangle is:", rectangle_area)  # Output: 50

# with open("my_document.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("report.txt", "w") as file:
#     file.write("This is my report.\n")
#     file.write("Python is awesome!\n")

# with open("report.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("application.log", "a") as file:
#     file.write("User logged in\n")
#     file.write("User clicked button\n")

# file_name = input("Enter the file name you want to read: ")

# try:
#     with open(f"{file_name}", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("This file not found")

# file_name = input("Enter file name: ")

# with open(file_name, "w") as file:
#     while True:
#         line = input("Enter a line: ")
#         if line == "DONE":
#             break
#         file.write(line + "\n")  # faylga yoz

# file_name = input("Enter file name: ")

# with open(file_name, "a") as file:
#     while True:
#         line = input("Enter a line: ")
#         if line == "DONE":
#             break
#         file.write(line + "\n")  # faylga yoz

# from datetime import datetime

# file_name = input("Enter file name: ")

# with open(file_name, "a") as file:
#     message = input("Enter a log message: ")
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     file.write(f"[{timestamp}] {message}\n")

# from datetime import datetime

# file_name = input("Enter a file name: ")

# with open(file_name, "a") as file:
#     timer = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
#     message = input("message? ")
#     file.write(f"[{timer}] {message} \n")

# filename = "report.txt"

# try:
#     with open(filename, 'r') as file:
#         line = file.readline()
#         while line:
#             print(line.strip())
#             line = file.readline()
# except FileNotFoundError:
#     print(f"Error: The file '{filename}' was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# with open("report.txt", "r") as file:
#     chunk1 = file.read(10)
#     print(chunk1, "\n")
#     chunk2 = file.read(15)
#     print(chunk2)
    
# with open("report.txt", "r") as file:
#     content = file.read()
#     words ="".join(x for x in content if x.isalnum() or x.isspace())
#     words = words.split()
#     print(f"Word count: {len(words)}")

# def get_line(filename, line_number):
#     with open(filename, "r") as file:
#         for i in range(line_number):
#             line = file.readline()  # ← har safar bitta qator o'qiydi
#         return line

# # line_number out of range bo'lsa nima qaytaradi?
# print(get_line("report.txt", 5))

# def get_line(filename, line_number):
#     """Retrieves a specific line from a file.
#     Returns an error message if the line number is out of range.
#     """
#     try:
#         with open(filename, 'r') as file:
#             for i, line in enumerate(file, 1):
#                 if i == line_number:
#                     return line.strip()
#             return f"Error: Line {line_number} not found in the file."
#     except FileNotFoundError:
#         return f"Error: The file '{filename}' was not found."
#     except Exception as e:
#         return f"An error occurred: {e}"
# #Example usage of exercise 2
# file_name = "report.txt"
# line_number_to_get = 5
# line_content = get_line(file_name, line_number_to_get)
# print(f"Content of line {line_number_to_get}: {line_content}")


def chunked_processing(filename, chunk_size):
    try:
        with open(filename, "r") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                print(chunk)
    except FileNotFoundError:
        print("This file not found.")
    except Exception as e:
        print(f"Error occured - {e}")

chunked_processing("report.txt", 1024)