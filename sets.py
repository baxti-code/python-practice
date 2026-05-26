# my_sets = {1, 2, 3, 4, 5}
# print(type(my_sets))
# string_set = {"This", "is", "for", "test"}
# print(type(string_set))

# empty_set = set()
# print(empty_set)

# my_set = {1, 2, 3, 4}
# element = my_set.pop()
# print(element)

# # Creating a set of squares of numbers from 1 to 5
# squares = {x**2 for x in range(1, 6)}
# print(squares)  # Output: {1, 4, 9, 16, 25}

# # Creating a set of even numbers from a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = {x for x in numbers if x % 2 == 0}
# print(even_numbers)  # Output: {2, 4, 6, 8, 10}

# my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
# unique_list = list(set(my_list))  # Convert the set back to a list
# print(unique_list)  # Output: [1, 2, 3, 4, 5]


# text = "This is a sample text. This text is used to demonstrate set operations."
# #words = text.lower().split()  # Convert to lowercase and split into words
# new_text = "".join(c for c in text.lower() if c.isalnum() or c.isspace())
# words = new_text.split()
# unique_words = set(words)
# print(unique_words)
# print(len(unique_words))

# def unique_characters(text):
#     """
#     Returns a set of unique characters in the given string.
#     """

#     new_t = "".join(c for c in text.lower() if c.isalnum())
#     return set(new_t)

# print(unique_characters("he ?> llo"))  # Expected output: {'h', 'e', 'l', 'o'}
# print(unique_characters("programming? "))  # Expected output: {'g', 'm', 'i', 'r', 'o', 'n', 'p', 'a'}

# user1_friends = ["Alice", "Bob", "Charlie", "David"]
# user2_friends = ["Charlie", "David", "Eve", "Frank"]

# def common_friends(friends1, friends2):
#     """
#     Returns a list of common friends between two users.
#     """
#     return list(set(friends1).intersection(set(friends2)))

# print(common_friends(user1_friends, user2_friends))  # Expected output: ['Charlie', 'David']

# sentence1 = "The quick brown fox jumps over the lazy dog"
# sentence2 = "The lazy cat sleeps under the sun"

# def word_difference(sentence1, sentence2):
#     """
#     Returns a set of words present in sentence1 but not in sentence2.
#     """
#     words1 = set(sentence1.lower().split())
#     words2 = set(sentence2.lower().split())
#     return words1.difference(words2)


# print(word_difference(sentence1, sentence2))
# # Expected output: {'brown', 'fox', 'over', 'quick', 'dog', 'jumps'}


list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

def symmetric_difference_numbers(list1, list2):
    """
    Returns a set of numbers present in either list1 or list2, but not in both.
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.symmetric_difference(set2)

print(symmetric_difference_numbers(list1, list2))  # Expected output: {1, 2, 4, 6, 7, 8}