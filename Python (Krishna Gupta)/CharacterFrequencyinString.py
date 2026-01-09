def char_count(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

string = input("Enter a String:")
result = char_count(string)
print("Character Frequency:")
for k,v in result.items():
    print(k, ":", v)
