import random

# print(random.random())      # Output: A random float between 0.0 and 1.0
# print(random.randint(1, 10))  # Output: A random integer between 1 and 10
# print(random.uniform(1, 10))  # Output: A random float between 1 and 10


#choice()
# print(random.choice(("a", "b", "d")))
# print(random.choice("Hello"))
# print(random.choice([1, 2, 3, 4, 5]))


#shuffle

# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)

#sample

# print(random.sample(range(1,10), k=5))
# print(random.sample([1, 2, 3, 4, 5], k=3))
# print(random.sample("Hello", k=3))
# print(random.sample(("a", "b", "c"), k=2))


#randint

# print(random.randint(1, 10)) # 1 and 10 included
# Tanga tashlash
# coin = random.randint(0, 1)
# if coin == 0:
#     print("Heads")
# else:
#     print("Tails")


#uniform

# print(random.uniform(1, 10)) # float random number

# r_num = random.uniform(1, 100)
# print(f"Random number is {r_num:.2f}")

# Foiz
# discount = random.uniform(0.05, 0.30)
# print(f"Chegirma: {discount:.0%}")  # Chegirma: 18%

#seed

# random.seed(42)
# print(random.randint(1, 100))  # masalan 52
# print(random.randint(1, 100))  # masalan 31

# random.seed(42)                # qayta 42 ga qaytdik
# print(random.randint(1, 100))  # yana 52!
# print(random.randint(1, 100))  # yana 31!

#choices

# print(random.choices([1, 2, 3, 4, 5], k=3)) #numbers can be repeated

# O'yin: 60% regular, 30% Good, 10% Great
# loot = random.choices(
#     ["Regular", "Good", "Great"],
#     weights=[60, 30, 10],
#     k=1
# )
# print(loot)  # mostly Regular

#Trying 1000 times

results = random.choices(["Heads", "Tails"], weights=[70, 30], k=1000)

heads = results.count("Heads")
tails = results.count("Tails")
print(f"Heads: {heads/10}%")   # ~70%
print(f"Tails: {tails/10}%")   # ~30%


#difference between choices and sample

# random.choices([1,2,3], k=3)  # [2, 2, 1] ← with replacement
# random.sample([1,2,3], k=3)   # [2, 3, 1] ← without replacement