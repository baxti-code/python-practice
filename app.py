# movies = ["Bridge to Teresmthing", "lightning McQueen", "Panda", "Rush Hour", "Prison Break", "Breaking Bad", "Into the wild"]
# for movie in movies:
#     print(movie)
# word = input("enter a word: ")
# reversed_word = word[::-1]
# for char in reversed_word:
#     print(char)

# for number in range(10, 20):
#     if number % 2 == 1:
#         print(number)

# import random

# number = random.randint(1,100)
# attempts = 0

# while True:
#     user_number = int(input("Enter a number between 1-100: "))
#     if user_number == number:
#         print("You found it!")
#         break
#     elif user_number > number:
#         print(f"Number is less than {user_number} ")
#     elif user_number < number:
#         print(f"The number is greater than {user_number}")
#     attempts+=1
#     print(f"Number of attempts : {attempts}")


# for row in range(1, 11):
#     for col in range(1, 11):
#         print(f"{row * col:4}", end="")
#     print()

# Example: Searching for a specific number in a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 5

# for number in numbers:
#     print(f"Checking number: {number}")
#     if number == target:
#         print(f"Found the target: {target}")
#         break  # Exit the loop when the target is found
#     else:
#         print(f"{number} is not the target.")

# print("Loop finished.")

# Example: Validating user input
# while True:
#     user_input = input("Enter a number (or 'q' to quit): ")

#     if user_input.lower() == 'q':
#         break  # Exit the loop if the user enters 'q'

#     try:
#         number = float(user_input)  # Convert the input to a float
#         print(f"You entered: {number}")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#         continue  # Skip to the next iteration if the input is not a number

# numbers = range(1,20)
# for number in numbers:
#     if number ==10:
#         break
#     if number % 2 ==0:
#         continue
#     print(number)


# text = input("Enter a text: ")
# for char in text:
#     if char.lower() in ("a", "e", "i", "o", "u"):
#         continue
#     print(char, end="\t")

# numbers = [11, 0, -1, -4, 4, -34, -98, 11]
# sum_num = 0
# for number in numbers:
#     if number <=0:
#         continue
#     sum_num=sum_num+number
# print(sum_num)

# for i in range(1,5):
#     print(f"Outer loop value : {i}")
#     for j in range(1,5):
#         if j * i >12:
#             print("Breaking out of the inner loop")
#             break
#         print(f"Inner loop value: {j}")

# import random

# secret_number = random.randint(1,100)
# number_of_attempts = 0

# while True:
#     guess = int(input("Guess the number: "))
#     number_of_attempts+=1
#     print(f"Number of attempts : {number_of_attempts}")
#     if guess == secret_number:
#         print(f"Congrats, you found the secret number {secret_number} in {number_of_attempts} attempts")
#         break
#     elif guess > secret_number:
#         print("Too high")
#     elif guess < secret_number:
#         print("Too low")
import random

def play_guessing_game():
    while True:
        while True:
            difficulty_level = input("Choose difficulty level (Easy/Medium/Hard): ").lower()
            if difficulty_level == "easy":
                lower_bound, upper_bound = 1, 10
            elif difficulty_level == "medium":
                lower_bound, upper_bound = 1, 100
            elif difficulty_level == "hard":
                lower_bound, upper_bound = 1, 1000
            else:
                print("Enter a valid level")
                continue
            secret_number = random.randint(lower_bound, upper_bound)
            break

        print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. You have 7 attempts.")
        guess_count = 0

        while True:
            try:
                guess = int(input("Take a guess: "))
                guess_count += 1
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                continue

            if guess_count <= 7:  # ← tuzatildi
                if guess < secret_number:
                    print("Too low!")
                elif guess > secret_number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed in {guess_count} attempts!")
                    break
            else:
                print(f"You lose! The secret number was {secret_number}")
                break
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ("yes", "y"):
            continue  # ← o'yinni qayta boshlaydi
        else:
            print("Thanks for playing!")
            break  # ← chiqadi
play_guessing_game()