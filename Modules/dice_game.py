import random

number_of_times = int(input("How many times do you want to roll a dice : "))
total = 0

dice_faces = {
    1: "⚀ (One)",
    2: "⚁ (Two)",
    3: "⚂ (Three)",
    4: "⚃ (Four)",
    5: "⚄ (five)",
    6: "⚅ (Six)"
}

print("\n--- Results ---")
for each in range(number_of_times):
    n = random.randint(1, 6)
    total += n
    print(f"{each + 1}-roll: {dice_faces[n]}")
    
print("-" * 17)
print(f"Total value: {total}")