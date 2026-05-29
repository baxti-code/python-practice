# # # def outer_function():
# # #   # 'outer_var' is local to outer_function
# # #   outer_var = 20

# # #   def inner_function():
# # #     # 'inner_var' is local to inner_function
# # #     inner_var = 30
# # #     # inner_function can access outer_var
# # #     print("Value of outer_var inside inner_function:", outer_var)
# # #     print("Value of inner_var inside inner_function:", inner_var)

# # #   inner_function()
# # #   # This will cause an error because 'inner_var' is not defined in the scope of outer_function
# # #   # print("Value of inner_var outside inner_function:", inner_var)

# # # outer_function()

# # # def outer_function():
# # #     outer_var = 10

# # #     def inner_function():
# # #         nonlocal outer_var  # Refer to outer_var from the enclosing scope
# # #         outer_var = 20
# # #         print("Value of outer_var inside inner_function:", outer_var)

# # #     inner_function()
# # #     print("Value of outer_var inside outer_function:", outer_var)

# # # outer_function()

# # discount_rate = 0.1  # Global variable for discount rate

# # def calculate_price(price, quantity):
# #     """Calculates the total price after applying a discount."""
# #     global discount_rate # Use the global variable

# #     # Apply discount
# #     discount = price * discount_rate
# #     final_price = (price - discount) * quantity
# #     return final_price

# # # Example usage
# # price = 100
# # quantity = 5
# # total_price = calculate_price(price, quantity)
# # print("Total price:", total_price) # Output: 450.0

# def counter():
#     count = 0 # This is enclosed in counter

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment

# # Create an instance of the counter
# my_counter = counter()

# # Call the increment function multiple times
# print(my_counter()) # Output: 1
# print(my_counter()) # Output: 2
# print(my_counter()) # Output: 3


# def pizza_order():
#     items = []
    
#     def add_item(item):
#         items.append(item)
#         return items
    
#     return add_item  # ← add_item ni tashqariga chiqaramiz

# my_order = pizza_order()  # my_order = add_item funksiyasi

# print(my_order("Pizza"))         # ['Pizza']
# print(my_order("Cola"))          # ['Pizza', 'Cola']
# print(my_order("Salad"))         # ['Pizza', 'Cola', 'Salad']

# def pizza_order():
#     items = []
    
#     def add_item():
#         items.append("Pizza")  # faqat bir marta, o'zgartirib bo'lmaydi
    
#     add_item()  # ← ichkarida ishlatildi, tashqariga chiqmadi
#     return items

# print(pizza_order())  # ['Pizza'] — har safar yangi buyurtma!

# def bank_account():
#     balance = 1000  # ← tashqaridan o'zgartirib bo'lmaydi!
    
#     def deposit(amount):
#         nonlocal balance
#         balance += amount
#         return balance
    
#     return deposit

# my_account = bank_account()
# print(my_account(500))   # 1500
# # balance ga bevosita kira olmaysiz — himoyalangan!

# discount_rate = 0.1  # Global variable for discount rate

# def calculate_price(price, quantity):
#     """Calculates the total price after applying a discount."""
#     global discount_rate # Use the global variable

#     # Apply discount
#     discount = price * discount_rate
#     final_price = (price - discount) * quantity
#     return final_price

# # Example usage
# price = 100
# quantity = 5
# total_price = calculate_price(price, quantity)
# print("Total price:", total_price) # Output: 450.0

# def calculate_price(price, quantity, discount_rate):
#     discount = price * discount_rate
#     total_price = (price - discount) * quantity
#     return total_price

# price = 100
# quantity = 10
# discount_rate = 0.2
# print(calculate_price(price, quantity, discount_rate))

# def grandparent():
#     age = 60
#     def parent():
#         nonlocal age
#         age = age - 20
#         def child():
#             nonlocal age
#             print(f"Child output {age}")
#         child()
#     parent()
# grandparent()

PI = 3.14159
def calculate_circle_area(radius):
    area = PI * radius**2
    return area
print(calculate_circle_area(5))