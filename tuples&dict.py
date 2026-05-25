# def mid_point(point1, point2):
#     x = (point1[0] + point2[0]) / 2
#     y = (point1[1] + point2[1]) / 2
#     return (x, y)

# result = mid_point((1, 2), (3, 4))
# print(result)  # (2.0, 3.0)

# data = {"Baxti": (99, 90, 87, 100), "Ozod": (70, 60, 65, 50), "Berdi": (90,80, 60, 70), "Aziz": (90, 82, 75, 67)}

# def average(data):
#     for name, grades in data.items():
#         avg = sum(grades)/ len(grades)
#         print(f"{name} : {avg:.2f}")
    
    
# print(average(data))

# colors = {
#     (255, 0, 0): "Red",
#     (0, 255, 0): "Green",
#     (0, 0, 255): "Blue",
#     (2, 1, 200): "Black",
#     (3, 1, 800): "Pink"
# }

# def color_name(rgb):
#     return colors.get(rgb, "Unknown")

# print(color_name((255, 0, 0)))


costs = [("banana", 25), ("apple", 20), ("cherry", 15), ("strawberry", 30)]

def unpacker(costs):
    for name, cost in costs:
        print(f"{name} : {cost} sum")

unpacker(costs)