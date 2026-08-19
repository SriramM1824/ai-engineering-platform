import json
from file_utils import inspect_file

filename = input("Enter the filename: ")

metadata = inspect_file(filename)
print(metadata)

with open("data/sample.json", "r") as json_file:
    data = json.load(json_file)

print(data)

with open("data/output.json", "w") as json_file:
    json.dump(data, json_file)

