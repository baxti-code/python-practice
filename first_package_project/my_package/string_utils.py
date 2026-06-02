def reverse_string(text):
    reverse_text = text[::-1]
    return reverse_text

def is_palindrome(text):
    reverse_text = text[::-1]
    if reverse_text.lower() == text.lower():
        return "Palindrome"
    else:
        return "Not a palindrome"

def count_vowels(text):
    number_vowels = 0
    for char in text.lower():
        if char in ("a", "e", "i", "u", "o"):
            number_vowels+=1
    return number_vowels