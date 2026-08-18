import os

filename = input("Enter the filename: ")

if os.path.exists(filename):
    print("File exists.")
    extension = os.path.splitext(filename)[1]
    print(f"File extension: {extension}")
else:
    print("File does not exist.")