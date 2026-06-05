# import json

# # Python dict
# person = {
#     "name": "Baxti",
#     "age": 19,
#     "city": "Tashkent"
# }

# # Dict → JSON string
# json_string = json.dumps(person)
# print(json_string)
# print(type(json_string))

# import json

# person = {
#     "name": "Baxti",
#     "age": 19,
#     "city": "Tashkent"
# }

# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)  # indent → chiroyli formatda yozadid

# import json

# with open("person.json", "r") as file:
#     person = json.load(file)  # JSON fayl → dict

# print(person)
# print(type(person))
# print(person["name"])

# import statistics

# numbers = [2, 4, 6, 8, 10, 4, 6]

# print(statistics.mean(numbers))     # o'rtacha → 5.71
# print(statistics.median(numbers))   # o'rta qiymat → 6
# print(statistics.mode(numbers))     # eng ko'p takrorlangan → 4 va 6
# print(statistics.stdev(numbers))    # standart og'ish
# print(statistics.variance(numbers)) # dispersiya

import string
import random

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(12))
print(password)  # xG#9kL@2mP!q
