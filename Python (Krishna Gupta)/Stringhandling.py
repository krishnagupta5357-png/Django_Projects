#Accessing Characters
name="python"
print(name[0])
print(name[-2])

#String Slicing
text= "programming"
print(text[0:5])
print(text[:4])
print(text[5:])

#String Concatenation and Repitition
s1= "I"
s2= "Love"
s3= "India"
print(s1+  " " +s2+  " " +s3)
print(s3*3)

#String Length
msg="Krishna"
print(len(msg))

#String Case Methods
text="programming"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

#Search and Replace
sentence="Python is Programming"
print(sentence.find("i"))
print(sentence.find("s"))
print(sentence.replace("Programming", "Simple"))

#String Testing Methods
s="abc123"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print("PYTHON".islower())

#Strip and Split
data= "  Hello World   "
print(data.strip())

text="apple, banana, mango"
print(text.split())

#Join
words=["Python", "is","Programming"]
print(" ".join(words))

#Looping Through String
for char in "Krishna":
    print(char)

