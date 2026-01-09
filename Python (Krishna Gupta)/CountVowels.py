def count_vowels(s):
    """Count vowels in a string"""
    count = 0
    for char in s.lower():
        if char in "aieou":
            count += 1
    return count
print("2. Vowels Count:", count_vowels("Hello Krishna"))