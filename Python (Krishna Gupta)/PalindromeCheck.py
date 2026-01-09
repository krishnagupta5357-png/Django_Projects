def is_palindrome(s):
    """Check if a String is Palindrome"""
    return s == s[::-1]
print("1. Palindrome:", is_palindrome("DAY"))