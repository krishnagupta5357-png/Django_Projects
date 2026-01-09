try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: The File You are Trying to Open does not Exist.")